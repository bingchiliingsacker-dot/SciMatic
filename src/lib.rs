mod flicker;
mod conversion;

use pyo3::prelude::*;

#[pymodule]
fn flicker_module(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(flicker::flick, m)?)?;
    Ok(())
}

#[pymodule]
fn rs_converters(m: &Bound<'_, PyModule>) -> PyResult<()> {
				m.add_function(wrap_pyfunction!(b2b::convert_binary, m)?)?;
				Ok(())
}