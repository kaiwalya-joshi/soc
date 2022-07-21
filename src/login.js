import React, { Component } from 'react'
import App from './App'  

export default class Login extends Component {

    constructor(){
        super();
        this.state = {
          username: "",
          password: "",
          ispressed : false,
          final_username: "",
          final_password: ""
        }    
      }
    

    handleInputChangedusername(event) {
        this.setState({
          username: event.target.value
        });
      }
    
      handleInputChangedpassword(event) {
        this.setState({
          password: event.target.value
        });
      }

      handlesubmit = () => {
        this.setState({
          ispressed:true,
        })
      } 

    render() {
      return (        
            
             <div className='mt-5 text-white'>
                
              <form className='container bg-dark p-5'>
                
                <div className="form-outline mb-4">
                    <label className="form-label" name = "username">UserName</label>
                    <input type="text" id="form2Example1" className="form-control" value={this.state.username} onChange={this.handleInputChangedusername.bind(this)}/>
                </div>

                <div className="form-outline mb-4">
                    <label className="form-label" name = "password">Password</label>
                    <input type="password" id="form2Example2" className="form-control" value={this.state.password} onChange={this.handleInputChangedpassword.bind(this)}/>
                </div>
                {console.log(this.state.username)}
                {console.log(this.state.password)}
                <button className='btn btn-danger btn-block'>
                        <a href="http://127.0.0.1:3000/" className='text-decoration-none text-white'>submit</a>
                </button>
                <div>
                    <p>Don't have account? Join us for latest News !!!</p>
                    <button className="btn btn-primary btn-block mb-4 m-3">
                        <a href="http://127.0.0.1:8000/signup" className='text-decoration-none text-white'>Sign up</a>
                    </button>
                </div>
                </form>

                
                
            </div> 
            
      )
    }
  } 