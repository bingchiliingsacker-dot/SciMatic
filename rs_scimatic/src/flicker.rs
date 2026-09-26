use pyo3::prelude::*;
use pyo3::types::PyList;

#[pyfunction]
#[pyo3(signature = (vectorbools, binary=false))]
pub fn flick(
    py: Python<'_>,
    vectorbools: Vec<Py<PyAny>>,
    binary: bool,
) -> PyResult<Py<PyList>> {
    let output = PyList::empty(py);

    for b in vectorbools {
        if binary {
            let v: u8 = b.extract(py)?;
            output.append(if v == 0 { 1 } else { 0 })?;
        } else {
            let v: bool = b.extract(py)?;
            output.append(!v)?;
        }
    }

    Ok(output.unbind())
}
