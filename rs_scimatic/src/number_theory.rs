use pyo3::prelude::*;

fn gcd_calc(mut a: i64, mut b: i64) -> i64 {
    while b != 0 {
        let remainder = a % b;
        a = b;
        b = remainder;
    }

    a.abs()
}
#[pyfunction]
pub fn gcd(
    py: Python<'_>,
    a: i64,
    b: i64,
    print_result: bool
) -> PyResult<i64> {
    let output = gcd_calc(a, b);

    if print_result {
        let builtins = py.import("builtins")?;
        builtins.call_method1("print", (output,))?;
    }

    Ok(output)
}

#[pyfunction]
pub fn lcm(
    py: Python<'_>,
    a: i64,
    b: i64,
    print_result: bool
) -> PyResult<i64> {
    let output = if a == 0 || b == 0 {
        0
    } else {
        (a / gcd_calc(a, b)) * b
    };

    if print_result {
        let builtins = py.import("builtins")?;
        builtins.call_method1("print", (output,))?;
    }

    Ok(output)
}