import { useEffect, useState } from 'react'
import './App.css'

function App() {
  const [time, setTime] = useState()
  useEffect(() => {
    fetch('/time')
      .then((res) => res.json())
      .then((data) => {
        setTime(data.time)
        console.log(data.time)
      })
  }, [])
  return (
    <div className="App">
      <header className="App-header">
        Hello From Sabari Vignesh & Suhaas
        <br />
        <div style={{ marginTop: '35px' }}>Time Is</div>
        {time && <h2>{time}</h2>}
      </header>
    </div>
  )
}

export default App
