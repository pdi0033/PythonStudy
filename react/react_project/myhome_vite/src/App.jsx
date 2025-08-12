import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import Counter from './components/counter'
import {Link, Routes, Route, Outlet} from "react-router-dom"
import "bootstrap/dist/css/bootstrap.min.css"

import Home from "./pages/home"  // 확장자 생략
import About from './pages/about'
import Nomatch from './pages/nomatch'
import ScoreList from './components/score/score_list'
import ScoreWrite from './components/score/score_write'
import TodoList from './components/todos/todo_list'

function App() {
  const [count, setCount] = useState(0)

  return (
    <div className='container-fluid'>
      <nav style={{display:'flex', gap:'1rem', marginBottom:'1rem'}}>
        <Link to='/'>Home</Link>
        <Link to='/about'>About</Link>
        <Link to='/counter'>Counter</Link>
        <Link to='/score/list'>성적처리</Link>
        <Link to='/score/insert'>성적추가</Link>
        <Link to='/todo/list'>할일</Link>
      </nav>

      {/* Routes - 경로, url -> 특정 컴포넌트와 연결하는 작업 */}
      <Routes>
        <Route path='/' element={<Home/>} />
        <Route path='/about' element={<About/>} />
        <Route path='/counter' element={<Counter/>} />
        <Route path='/score/list' element={<ScoreList/>} />
        <Route path='/score/insert' element={<ScoreWrite/>} />
        <Route path='/todo/list' element={<TodoList/>} />
        <Route path='*' element={<Nomatch/>} />
      </Routes>
      {/* url을 바꾸면 컴포넌트가 출력될 위치 */}

      <Outlet />

    </div>
  )
}

export default App
