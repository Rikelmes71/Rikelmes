import './styles.css'
import LoginPage from './pages/LoginPage'
import DashboardPage from './pages/DashboardPage'
import IntegrationsPage from './pages/IntegrationsPage'
import LogsPage from './pages/LogsPage'
import ManualModePage from './pages/ManualModePage'
import UsersPage from './pages/UsersPage'

export default function App() {
  return (
    <main className="app-shell">
      <header className="app-header">
        <h1>CS Brasil - Automação Reserve</h1>
        <p>Interface com identidade visual focada no azul corporativo da CS Brasil.</p>
      </header>

      <section className="grid">
        <LoginPage />
        <DashboardPage />
        <IntegrationsPage />
        <LogsPage />
        <ManualModePage />
        <UsersPage />
      </section>
    </main>
  )
}
