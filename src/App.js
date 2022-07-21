import './App.css';
import React, { Component } from 'react'
import { Route } from 'react-router-dom'
import NavBar from './component/NavBar';
import News from './component/News';
import axios from "axios";
import Login from './login';



export default class App extends Component {
  persons = []  
  
  
  constructor(){
    super();
    this.state = {
      persons : this.persons,
      isLoggedIn: true
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

  async componentDidMount(){
    
    
      let data = await fetch('http://127.0.0.1:8000/api/persons/');
      data = await data.json();
      this.setState({persons: data})
      console.log(data)
    
  }
     
   

      
  render() {
    // let {username, password} = this.props;
    
    // let data_filter = this.state.persons.filter( element => element.username === username);
    // let data_filter2 = data_filter.filter(element => element.password === password);
    // this.setState({
    //   isLoggedIn: data_filter2.isLoggedIn
    // });
    return (
      <div>
      {/* <div className='mt-5 text-white'>
              <form className='container bg-dark p-5' method = 'POST'>

                <div className="form-outline mb-4">
                    <label className="form-label" name = "username">UserName</label>
                    <input type="email" id="form2Example1" className="form-control" value={this.state.username} onChange={this.handleInputChangedusername.bind(this)}/>
                </div>

                <div className="form-outline mb-4">
                    <label className="form-label" name = "password">Password</label>
                    <input type="password" id="form2Example2" className="form-control" value={this.state.password} onChange={this.handleInputChangedpassword.bind(this)}/>
                </div>

                
                </form>
            </div> 
             */}
          <div>
            <NavBar/>
            <News isLoggedIn = {true}/>
          </div> 
        </div>
    )
  }
}



  // else redirect to login page


