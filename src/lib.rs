use pyo3::prelude::*;
use pyo3::types::PyList;

#[pyfunction]
#[pyo3(signature = (vectorbools, binary=false))]
fn flick(
    py: Python<'_>,
    vectorbools: Vec<bool>,
    binary: bool,
) -> PyResult<Py<PyList>> {
    let output = PyList::empty(py);

    for b in vectorbools {
        if binary {
            output.append(if b { 0 } else { 1 })?;
        } else {
            output.append(!b)?;
        }
    }

    Ok(output.unbind())
}

#[pymodule]
fn flicker_module(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(flick, m)?)?;
    Ok(())
}
