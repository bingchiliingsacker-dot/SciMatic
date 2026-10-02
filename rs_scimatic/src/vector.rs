use pyo3::prelude::*;

#[pyclass]
pub struct Vector {
    x: i64,
    y: i64,
}

#[pymethods]
impl Vector {
    #[new]
    fn new(x: i64, y: i64) -> Self {
        Self {
            x,
            y
        }
    }

    fn magnitude(
        &self,
        py: Python<'_>,
        print_result: bool,
    ) -> PyResult<f64> {
        let x: f64 = self.x as f64;
        let y: f64 = self.y as f64;

        let output = (x.powi(2) + y.powi(2)).sqrt();

        if print_result {
            let builtins = py.import("builtins")?;
            builtins.call_method1("print", (output,))?;
        }

        Ok(output)
    }

    fn normalize(
        &self,
        py: Python<'_>,
        print_result: bool
    ) -> PyResult<(f64, f64)> {
        let mg: f64 = self.magnitude(py, false)?;
        let x: f64 = self.x as f64;
        let y: f64 = self.y as f64;

        if x == 0.0 && y == 0.0 {
            let builtins = py.import("builtins")?;
            builtins.call_method1("print", ("💥 SciMatic Failed.\n\n☝️ Reason: Cannot divide by zero.\n💡 Tip: Change the coordinates to a nonzero.", ))?;
            return Err(pyo3::exceptions::PyZeroDivisionError::new_err("Cannot Divide by 0. Refer to the text above for more information."));
        }

        let output: (f64, f64) = (x / mg, y / mg);

        if print_result {
            let builtins = py.import("builtins")?;
            builtins.call_method1("print", (output,))?;
        }
        Ok(output)
    }

    fn dot(
        &self,
        py: Python<'_>,
        other: &Vector,
        print_result: bool
    ) -> PyResult<f64> {
        let x1: f64 = self.x as f64;
        let y1: f64 = self.y as f64;

        let x1x2: f64 = x1 * other.x as f64;
        let y1y2: f64 = y1 * other.y as f64;

        let output: f64 = x1x2 + y1y2;

        if print_result {
            let builtins = py.import("builtins")?;
            builtins.call_method1("print", (output,))?;
        }

        Ok(output)
    }

    fn distance(
        &self,
        py: Python<'_>,
        other: &Vector,
        print_result: bool
    ) -> PyResult<f64> {
        let x1: f64 = self.x as f64;
        let y1: f64 = self.y as f64;

        let x: f64 = other.x as f64 - x1;
        let y: f64 = other.y as f64 - y1;

        let d: f64 = (x.powi(2) + y.powi(2)).sqrt();

        if print_result {
            let builtins = py.import("builtins")?;
            builtins.call_method1("print", (d,))?;
        }

        Ok(d)
    }

    fn angle(
        &self,
        py: Python<'_>,
        other: &Vector,
        print_result: bool
    ) -> PyResult<f64> {
        let dot: f64 = self.dot(py, other, false)?;
        let mag_a: f64 = self.magnitude(py, false)?;
        let mag_b: f64 = self.magnitude(py, false)?;

        if mag_a == 0.0 || mag_b == 0.0 {
            let builtins = py.import("builtins")?;
            builtins.call_method1("print", ("💥 SciMatic Failed.\n\n☝️ Reason: Cannot divide by zero.\n💡 Tip: Change the coordinates to a nonzero.", ))?;
            return Err(pyo3::exceptions::PyZeroDivisionError::new_err("Cannot Divide by 0. Refer to the text above for more information."));
        }

        let cosine: f64 = dot / (mag_a * mag_b);
        let angle: f64 = cosine.acos().to_degrees();

        if print_result {
            let builtins = py.import("builtins")?;
            builtins.call_method1("print", (angle,))?;
        }

        Ok(angle)
    }

    fn scale(
        &self,
        py: Python<'_>,
        scalar: f64,
        print_result: bool
    ) -> PyResult<(f64, f64)> {
        let x: f64 = self.x as f64;
        let y: f64 = self.y as f64;

        let output: (f64, f64) = (x * scalar, y * scalar);

        if print_result {
            let builtins = py.import("builtins")?;
            builtins.call_method1("print", (output,))?;
        }
        Ok(output)
    }
}