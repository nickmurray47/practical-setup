import { useEffect, useState } from 'react'
import { listTodos, addTodo, toggleTodo, deleteTodo } from './api'

export default function App() {
  const [todos, setTodos] = useState([])
  const [text, setText] = useState('')

  async function refresh() { setTodos(await listTodos()) }
  useEffect(() => { refresh() }, [])

  async function onAdd(e) {
    e.preventDefault()
    if (!text.trim()) return
    await addTodo(text.trim())
    setText('')
    refresh()
  }

  return (
    <div style={{maxWidth: 600, margin: '40px auto', padding: '0 20px', fontFamily: 'system-ui, sans-serif'}}>
      <h1>Full-Stack Template</h1>
      <form onSubmit={onAdd} style={{display:'flex', gap:8}}>
        <input value={text} onChange={e=>setText(e.target.value)} placeholder="Add a todo..." style={{flex:1}}/>
        <button>Add</button>
      </form>
      <ul style={{marginTop:16, paddingLeft:0, listStyle: 'none'}}>
        {todos.map(t => (
          <li key={t.id} style={{display:'flex', alignItems:'center', gap:8, margin:'8px 0', padding: '12px', border: '1px solid #404040', borderRadius: '8px', backgroundColor: '#2a2a2a'}}>
            <input type="checkbox" checked={t.done} onChange={()=>toggleTodo(t.id, !t.done).then(refresh)} />
            <span style={{textDecoration: t.done ? 'line-through' : 'none', flex: 1}}>{t.text}</span>
            <button onClick={()=>deleteTodo(t.id).then(refresh)} style={{padding: '4px 8px', backgroundColor: '#ff4444', color: 'white', border: 'none', borderRadius: '4px', cursor: 'pointer'}}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  )
}
