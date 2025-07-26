import { useRef, useState } from 'react'
import './App.css'

function App() {
  const [count, setCount] = useState(0)
  const inputReference = useRef<HTMLInputElement | null>(null)
  const outputFieldReference = useRef<HTMLParagraphElement | null>(null)
  
  const clickSend = () => {
    const inputNumber = inputReference.current!.value;
    fetch('http://127.0.0.1:8000/api/process_number',{
      method: 'POST',
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({my_number: inputNumber})
  })
    .then(x=>x.json().then(j => 
      outputFieldReference.current!.innerText= j["new_number"]))
  }

  return (
    <>
      <div className="card">
        <button onClick={() => setCount((count) => count + 1)}>
          count is {count}
        </button>
        <input ref={inputReference}></input>
        <button onClick={clickSend} >Send</button>
        <p ref={outputFieldReference}></p>
        <p>
          Edit <code>src/App.tsx</code> and save to test HMR
        </p>
      </div>
    </>
  )
}

export default App
