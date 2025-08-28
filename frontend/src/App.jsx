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
    <div style={{maxWidth: 600, margin: '40px auto', fontFamily: 'system-ui, sans-serif'}}>
      <h1>Full-Stack Template</h1>
      <form onSubmit={onAdd} style={{display:'flex', gap:8}}>
        <input value={text} onChange={e=>setText(e.target.value)} placeholder="Add a todo..." style={{flex:1}}/>
        <button>Add</button>
      </form>
      <ul style={{marginTop:16, paddingLeft:18}}>
        {todos.map(t => (
          <li key={t.id} style={{display:'flex', alignItems:'center', gap:8, margin:'8px 0'}}>
            <input type="checkbox" checked={t.done} onChange={()=>toggleTodo(t.id, !t.done).then(refresh)} />
            <span style={{textDecoration: t.done ? 'line-through' : 'none'}}>{t.text}</span>
            <button onClick={()=>deleteTodo(t.id).then(refresh)} style={{marginLeft:'auto'}}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  )
}
