export async function listTodos() {
    const r = await fetch('/api/todos')
    return r.json()
  }
  export async function addTodo(text) {
    const r = await fetch('/api/todos', {
      method: 'POST',
      headers: {'Content-Type':'application/json'},
      body: JSON.stringify({ text })
    })
    return r.json()
  }
  export async function toggleTodo(id, done) {
    const r = await fetch(`/api/todos/${id}`, {
      method: 'PATCH',
      headers: {'Content-Type':'application/json'},
      body: JSON.stringify({ done })
    })
    return r.json()
  }
  export async function deleteTodo(id) {
    await fetch(`/api/todos/${id}`, { method: 'DELETE' })
  }
  