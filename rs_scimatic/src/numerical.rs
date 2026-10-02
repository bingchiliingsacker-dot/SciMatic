use pyo3::prelude::*;

#[pyfunction]
pub fn clamp(
    py: Python<'_>,
    x: f64,
    a: f64,
    b: f64,
    print_result: bool,
) -> PyResult<f64> {
    let processor = if x < a { a } else { x };
    let output = if processor > b { b } else { processor };

    if print_result {
        let builtins = py.import("builtins")?;
        builtins.call_method1("print", (output,))?;
    }

    Ok(output)
}

#[pyfunction]
pub fn lerp(
    py: Python<'_>,
    a: f64,
    b: f64,
    t: f64,
    print_result: bool
) -> PyResult<f64> {
    let output = a + (b - a) * t;

    if print_result {
        let builtins = py.import("builtins")?;
        builtins.call_method1("print", (output,))?;
    }

    Ok(output)
}