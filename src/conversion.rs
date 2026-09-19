use pyo3::prelude::*;
use pyo3::types::PyList;

#[pyfunction]
#[pyo3(signature = (b, print_result=false))]
pub fn convert_binary(
    py: Python<'_>,
    b: Vec<Py<PyAny>>,
    print_result: bool,
) -> PyResult<Py<PyList>> {
    let output = PyList::empty(py);

    for binary in b {
        if let Ok(value) = binary.extract::<bool>(py) {
            output.append(if value { 1 } else { 0 })?;
        } else if let Ok(value) = binary.extract::<u8>(py) {
            if value == 1 {
                output.append(true)?;
            } else if value == 0 {
                output.append(false)?;
            } else {
                return Err(pyo3::exceptions::PyValueError::new_err(
                    "Binary values must be 0 or 1",
                ));
            }
        } else {
            return Err(pyo3::exceptions::PyTypeError::new_err(
                "Expected bool or integer",
            ));
        }
    }

    if print_result {
        py.import("builtins")?
            .getattr("print")?
            .call1((output,))?;
    }

    Ok(output.unbind())
}
