mod flicker;
mod conversion;

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

	Ok(())
}
