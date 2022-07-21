import React from 'react';
import ReactDOM from 'react-dom/client'; 
import './index.css';
import App from './App';
import Login from './login'
import Signup from './signup'
import CheckMail from './check_mail';
import reportWebVitals from './reportWebVitals';
import { Route,  Routes, BrowserRouter as Router } from 'react-router-dom'  

// const root = ReactDOM.createRoot(document.getElementById('root'));
// root.render(
//   <React.StrictMode>
//     <App />
//   </React.StrictMode>
// );

// // If you want to start measuring performance in your app, pass a function
// // to log results (for example: reportWebVitals(console.log))
// // or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
// reportWebVitals();

// const routing = (  
//   <Router>  
//     <div>  
//       <h1>React Router Example</h1>  
//       <Route path="/" component={App} />  
//       <Route path="/login" component={Login} />    
//     </div>  
//   </Router>  
// )  



const root = ReactDOM.createRoot(document.getElementById('root')); 
root.render(
  <Router>  
    <Routes>   
      <Route path="/" element={<App />} />  
      <Route path="/login" element={<Login />} />    
      <Route path="/signup" element={<Signup />} />
      <Route path="/checkmail" element={<CheckMail />} />
    </Routes>  
  </Router>
)
reportWebVitals();