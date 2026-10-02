mod flicker;
mod conversion;
mod numerical;
mod number_theory;
pub mod vector;

use pyo3::prelude::*;

#[pymodule]
fn rs_scimatic(py: Python<'_>, m: &Bound<'_, PyModule>) -> PyResult<()> {
    let flicker_module = PyModule::new(py, "flicker")?;

    flicker_module.add_function(
        wrap_pyfunction!(flicker::flick, &flicker_module)?
    )?;

    m.add_submodule(&flicker_module)?;

    let conversion_module = PyModule::new(py, "conversion")?;

    conversion_module.add_function(
        wrap_pyfunction!(conversion::convert_binary, &conversion_module)?
    )?;

    m.add_submodule(&conversion_module)?;

    let numerical_module = PyModule::new(py, "numerical")?;

    numerical_module.add_function(
        wrap_pyfunction!(numerical::clamp, &numerical_module)?
    )?;

    numerical_module.add_function(
        wrap_pyfunction!(numerical::lerp, &numerical_module)?
    )?;

    numerical_module.add_submodule(&numerical_module)?;

    let number_theory_module = PyModule::new(py, "number_theory")?;

    number_theory_module.add_function(
        wrap_pyfunction!(number_theory::gcd, &number_theory_module)?
    )?;

    number_theory_module.add_function(
        wrap_pyfunction!(number_theory::lcm, &number_theory_module)?
    )?;

    number_theory_module.add_submodule(&number_theory_module)?;

    let vector_module = PyModule::new(py, "vector")?;

    vector_module.add_class::<vector::Vector>()?;

    m.add_submodule(&vector_module)?;

    Ok(())
}
