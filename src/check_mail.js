import React, { Component } from 'react'  
import OtpInput from 'react-otp-input';

export default class CheckMail extends Component {

    state = { otp: '' };

    handleChange = (otp) => {
      this.setState({ otp });
      console.log(this.state.otp);
    }

    render() {
      return (        
            <div className='container bg-dark mt-5 p-5'>
                <h3 className='text-center text-white'>Please check your mail and enter 6 digit code to confirm your email</h3>
                <form className='text-center' method = 'POST'>
                  <label className="text-white p-5">Enter 6 digit verification code</label>
                  <div className='d-flex justify-content-center'>
                    <OtpInput value={this.state.otp} onChange={this.handleChange} numInputs={6} separator={<span>-----</span>}/>
                  </div>
                  <input type="hidden" name="verification_code" value={this.state.otp} />
                  <button className='btn btn-primary btn-block m-5'>
                    <a href="../login" className='text-white text-decoration-none'>submit</a>
                  </button>
                </form>
            </div> 
      )
    }
  } 