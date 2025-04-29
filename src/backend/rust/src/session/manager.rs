use pyo3::prelude::*;
use tor_rtcompat::PreferredRuntime;

#[pyclass]
pub struct SessionManager {
    tor: Option<PreferredRuntime>,
}

#[pymethods]
impl SessionManager {
    #[new]
    fn new(tor_enabled: bool) -> Self {
        SessionManager {
            tor: if tor_enabled { Some(PreferredRuntime::current().unwrap()) } else { None },
        }
    }

    async fn create_session(&self, user_id: String) -> String {
        uuid::Uuid::new_v4().to_string()
    }

    async fn start(&self) {}
    async fn stop(&self) {}
}
