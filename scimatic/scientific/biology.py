"""Biological utilities for SciMatic."""

from itertools import product
from pathlib import Path
import sys
from ..utils.csv import CSV


def _default_path() -> Path:
    if sys.platform == 'win32':
        return Path.home() / 'Downloads'

    if sys.platform == 'android' or Path('/storage/emulated/0').exists():
        return Path('/storage/emulated/0') / 'Download'

    # Linux/macOS: honor XDG if set, else fall back to ~/Downloads
    import os
    xdg = os.environ.get('XDG_DOWNLOAD_DIR')
    return Path(xdg) if xdg else Path.home() / 'Downloads'


PATH = _default_path()
PATH.mkdir(parents=True, exist_ok=True)


class PunnettSquare:
    """Represent and analyze a Punnett square stored in a CSV file."""

    def __init__(self, file: str):
        if Path(file).suffix.lower() != '.csv':
            print('💥 SciMatic failed.')
            print('')
            print('☝ Reason: File suffix is not .csv.')
            print('💡 Tip: Use a .csv file.')
            raise ValueError('PunnettSquare requires a .csv file')

        self.csv = CSV(file)

    def cross(
            self
    ):
        raw = self.csv.read()
        processed = self.csv.deserialize(raw)

        special = {'i', 'I^A', 'I^B'}

        for j in range(1, len(processed)):
            for i in range(1, len(processed[j])):
                a1 = processed[0][i]
                a2 = processed[j][0]

                if a1 in special or a2 in special:
                    if a1 == 'i' and a2 == 'i':
                        gene = 'ii'
                    elif a1 == 'I^A' and a2 == 'I^A':
                        gene = 'I^AI^A'
                    elif a1 == 'I^B' and a2 == 'I^B':
                        gene = 'I^BI^B'
                    elif {a1, a2} == {'I^A', 'i'}:
                        gene = 'I^Ai'
                    elif {a1, a2} == {'I^B', 'i'}:
                        gene = 'I^Bi'
                    elif {a1, a2} == {'I^A', 'I^B'}:
                        gene = 'I^AI^B'
                    else:
                        gene = ''.join(sorted([a1, a2]))

                else:
                    gene = ''.join(sorted([a1, a2]))

                self.csv.replace_cell(
                    (i, j),
                    gene
                )

    def genotype_ratio(
            self,
            print_result: bool = False
    ) -> dict:

        raw = self.csv.read()
        processed = self.csv.deserialize(raw)

        hashmap = {}

        for j in range(1, len(processed)):
            for i in range(1, len(processed[j])):
                genotype = processed[j][i]
                hashmap[genotype] = hashmap.get(genotype, 0) + 1

        if print_result:
            print(hashmap)
        return hashmap

    def phenotype_ratio(
            self,
            dominant: dict | None,
            recessive: dict | None,
            bloodtype: bool = False,
            print_result: bool = False
    ) -> dict:
        if (dominant is None or recessive is None) and not bloodtype:
            print('💥 SciMatic failed.')
            print('')
            print('☝️ Reason: Dictionary `dominant` and `recessive` are required dictionaries.')
            print('💡 Tip: Either give them items corresponding to the table. Or if you are working with the ABO type case, set bloodtype to True.')
            raise ValueError('PhenotypeRatio requires a dominant and recessive dictionary.')
        raw = self.csv.read()
        processed = self.csv.deserialize(raw)

        hashmap = {}

        for j in range(1, len(processed)):
            for i in range(1, len(processed[j])):
                gene = processed[j][i]

                if bloodtype:
                    if gene in {'I^Ai', 'I^AI^A'}:
                        trait = 'A'
                    elif gene in {'I^Bi', 'I^BI^B'}:
                        trait = 'B'
                    elif gene == 'I^AI^B':
                        trait = 'AB'
                    elif gene == 'ii':
                        trait = 'O'
                    else:
                        print('💥 SciMatic failed.')
                        print('')
                        print('☝️ Reason: Invalid BloodType.')
                        print(
                            '💡 Tip: New to Punnett squares or need a refresher? Watch this video before using PunnettSquare:')
                        print('https://www.youtube.com/watch?v=WFjlPemOmFY')
                        raise ValueError(f'Invalid bloodtype genotype: {gene}')

                else:
                    if gene[0].isupper():
                        try:
                            trait = dominant[gene[0]]
                        except KeyError as exc:
                            print('💥 SciMatic failed.')
                            print('')
                            print('☝️ Reason: Dictionary `dominant` does not have a full list of all possible genes.')
                            print('💡 Tip: Try giving every Uppercased allele(Called dominant alleles in biology) a specific trait.')
                            raise KeyError(f'Key {gene[0]} is not found: {dominant}') from exc
                    else:
                        try:
                            trait = recessive[gene[0]]
                        except KeyError as exc:
                            print('💥 SciMatic failed.')
                            print('')
                            print('☝️ Reason: Dictionary `recessive` does not have a full list of all possible genes.')
                            print(
                                '💡 Tip: Try giving every Lowercased allele(Called recessive alleles in biology) a specific trait.')
                            raise KeyError(f'Key {gene[0]} is not found: {recessive}') from exc

                hashmap[trait] = hashmap.get(trait, 0) + 1

        if print_result:
            print(hashmap)
        return hashmap

    def probability(
            self,
            genotype: str,
            print_result: bool = False
    ) -> float:
        raw = self.csv.read()
        processed = self.csv.deserialize(raw)

        favorable_outcomes = 0
        number_of_outcomes = 0

        for j in range(1, len(processed)):
            for i in range(1, len(processed[j])):
                if processed[j][i] == genotype:
                    favorable_outcomes += 1
                number_of_outcomes += 1

        probability = (
            favorable_outcomes / number_of_outcomes
            if number_of_outcomes
            else 0.0
        )

        if print_result:
            print(f'Probability of {genotype}: {probability:.0%}')

        return probability


class DNA:
    """Represent and manipulate DNA sequences."""

    def __init__(self, strand: str):
        """Initialize a DNA sequence."""
        self.strand = strand.upper()

    def complement(
            self,
            max_iterations: int = 1_000_000,
            reverse_comp: bool = False,
            print_result: bool = False
    ) -> set:
        """Generate possible complementary DNA sequences."""
        base = {
            'A': 'T',
            'T': 'A',
            'C': 'G',
            'G': 'C'
        }
        ambiguity = {
            'R': {'A', 'G'},
            'Y': {'C', 'T'},
            'S': {'G', 'C'},
            'W': {'A', 'T'},
            'K': {'G', 'T'},
            'M': {'A', 'C'},
            'B': {'C', 'G', 'T'},
            'D': {'A', 'G', 'T'},
            'H': {'A', 'C', 'T'},
            'V': {'A', 'C', 'G'},
            'N': {'A', 'C', 'G', 'T'}
        }

        choices = []

        for s in self.strand:
            if s in ambiguity:
                choices.append(ambiguity[s])
            elif s in base:
                choices.append({base[s]})
            else:
                valid = ', '.join((*base.keys(), *ambiguity.keys()))
                print('💥 SciMatic failed.')
                print('')
                print('☝️ Reason: Letter is not a valid DNA nucleotide.')
                print(
                    f'💡 Tip: You must follow the IUPAC nucleotide code: {valid}'
                )
                raise ValueError(
                    'Invalid IUPAC nucleotide code. '
                    'Refer to the text above for more information.'
                )

        possibilities = 1

        for choice in choices:
            possibilities *= len(choice)

        if possibilities > max_iterations:
            print('💥 SciMatic failed.')
            print('')
            print(
                f'☝️ Reason: DNA strand would produce '
                f'{possibilities:,} possible sequences.'
            )
            print(
                '💡 Tip: Use a shorter strand or reduce the number '
                'of ambiguous bases.'
            )
            print('📋 Compilers note: Fuh naw I am not running that shit.')
            raise ValueError('Too many possible DNA sequences.')

        output = {
            ''.join(combo)
            for combo in product(*choices)
        }

        if reverse_comp:
            output = {
                ''.join(
                    {
                        'A': 'T',
                        'T': 'A',
                        'C': 'G',
                        'G': 'C'
                    }[base]
                    for base in o[::-1]
                )
                for o in output
            }

        if print_result:
            print(output)

        return output

    def DNA_to_mRNA(
            self,
            template: bool = False,
            max_iterations: int = 1_000_000,
            reverse_comp: bool = False,
            print_result: bool = False
    ) -> set:
        """Transcribe DNA into mRNA."""
        template_ = {
            'A': 'U',
            'T': 'A',
            'C': 'G',
            'G': 'C',
            'R': 'Y',
            'Y': 'R',
            'S': 'S',
            'W': 'W',
            'K': 'M',
            'M': 'K',
            'B': 'V',
            'D': 'H',
            'H': 'D',
            'V': 'B',
            'N': 'N'
        }

        coding = {
            'A': 'A',
            'T': 'U',
            'C': 'C',
            'G': 'G',
            'R': 'R',
            'Y': 'Y',
            'S': 'S',
            'W': 'W',
            'K': 'K',
            'M': 'M',
            'B': 'B',
            'D': 'D',
            'H': 'H',
            'V': 'V',
            'N': 'N'
        }

        choices = []

        for s in self.strand:
            if template:
                try:
                    choices.append({template_[s]})
                except KeyError as exc:
                    print('💥 SciMatic failed.')
                    print('')
                    print(
                        '☝️ Reason: Letter is not a valid DNA nucleotide.'
                    )
                    print(
                        f'💡 Tip: You must follow the IUPAC nucleotide code: '
                        f'{template_}'
                    )
                    raise ValueError(
                        'Invalid template sequence. '
                        'Refer to the text above for more information.'
                    ) from exc
            else:
                try:
                    choices.append({coding[s]})
                except KeyError as exc:
                    print('💥 SciMatic failed.')
                    print('')
                    print(
                        '☝️ Reason: Letter is not a valid DNA nucleotide.'
                    )
                    print(
                        f'💡 Tip: You must follow the IUPAC nucleotide code: '
                        f'{coding}'
                    )
                    raise ValueError(
                        'Invalid template sequence. '
                        'Refer to the text above for more information.'
                    ) from exc

        possibilities = 1

        for choice in choices:
            possibilities *= len(choice)

        if possibilities > max_iterations:
            print('💥 SciMatic failed.')
            print('')
            print(
                f'☝️ Reason: DNA strand would produce '
                f'{possibilities:,} possible sequences.'
            )
            print(
                '💡 Tip: Use a shorter strand or reduce the number '
                'of ambiguous bases.'
            )
            print('📋 Compilers note: Fuh naw I am not running that shit.')
            raise ValueError('Too many possible DNA sequences.')

        output = {
            ''.join(combo)
            for combo in product(*choices)
        }

        if reverse_comp:
            rna_complement = {
                'A': 'U',
                'U': 'A',
                'C': 'G',
                'G': 'C',
                'R': 'Y',
                'Y': 'R',
                'S': 'S',
                'W': 'W',
                'K': 'M',
                'M': 'K',
                'B': 'V',
                'D': 'H',
                'H': 'D',
                'V': 'B',
                'N': 'N'
            }

            output = {
                ''.join(
                    rna_complement[base]
                    for base in o[::-1]
                )
                for o in output
            }

        if print_result:
            print(output)

        return output

    def DNA_to_protein(
            self,
            template: bool = False,
            start_codon: bool = False,
            print_result: bool = False
    ) -> set:
        """Translate DNA into a protein sequence."""
        mrnas = self.DNA_to_mRNA(
            template=template
        )

        genetic_code = {
            'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
            'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
            'UAU': 'Y', 'UAC': 'Y', 'UAA': None, 'UAG': None,
            'UGU': 'C', 'UGC': 'C', 'UGA': None, 'UGG': 'W',

            'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
            'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
            'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
            'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',

            'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M',
            'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
            'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
            'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',

            'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
            'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
            'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
            'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
        }

        proteins = set()

        for mrna in mrnas:
            codons = [
                mrna[i:i + 3]
                for i in range(0, len(mrna) - 2, 3)
            ]

            protein = []

            for codon in codons:
                amino_acid = genetic_code[codon]

                if amino_acid is None:
                    break

                protein.append(amino_acid)

            output = ''.join(protein)

            if start_codon:
                start = output.find('M')

                if start == -1:
                    continue

                output = output[start:]

            proteins.add(output)

        if print_result:
            print(proteins)

        return proteins