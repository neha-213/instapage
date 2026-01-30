import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Instagram Demo",
    layout="wide"
)

html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>Instagram</title>
  <style>
    body{
      margin:0;
      font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
      background:#fafafa;
    }
    .wrapper{
      display:flex;
      justify-content:center;
      align-items:center;
      height:100vh;
    }
    .container{
      display:flex;
      gap:40px;
    }
    .phone{
      width:380px;
      height:580px;
      background:linear-gradient(135deg,#f09433,#e6683c,#dc2743,#cc2366,#bc1888);
      border-radius:20px;
      display:flex;
      justify-content:center;
      align-items:center;
      color:#fff;
      font-size:22px;
      font-weight:bold;
    }
    .login-area{
      width:350px;
    }
    .login-box{
      background:#fff;
      border:1px solid #dbdbdb;
      padding:40px;
      text-align:center;
    }
    .logo{
      font-family:cursive;
      font-size:50px;
      margin-bottom:30px;
    }
    input{
      width:100%;
      padding:9px;
      margin-bottom:8px;
      background:#fafafa;
      border:1px solid #dbdbdb;
      border-radius:3px;
      font-size:14px;
    }
    button{
      width:100%;
      padding:8px;
      background:#0095f6;
      border:none;
      border-radius:8px;
      color:#fff;
      font-weight:600;
      margin-top:10px;
      cursor:pointer;
    }
    .or{
      display:flex;
      align-items:center;
      margin:20px 0;
      color:#8e8e8e;
      font-size:13px;
      font-weight:600;
    }
    .or::before,.or::after{
      content:"";
      flex:1;
      height:1px;
      background:#dbdbdb;
      margin:0 10px;
    }
    .fb{
      color:#385185;
      font-weight:600;
      font-size:14px;
    }
    .forgot{
      font-size:12px;
      margin-top:15px;
      color:#00376b;
    }
    .error{
      color:#ed4956;
      font-size:14px;
      margin-top:15px;
    }
    .signup{
      background:#fff;
      border:1px solid #dbdbdb;
      padding:20px;
      margin-top:10px;
      text-align:center;
      font-size:14px;
    }
    .signup span{
      color:#0095f6;
      font-weight:600;
    }
    .success{
      background:#fff;
      border:1px solid #dbdbdb;
      padding:40px;
      text-align:center;
      display:none;
      width:350px;
    }
    .avatar{
      font-size:50px;
      margin:10px 0;
    }
    .bio{
      font-size:14px;
      color:#8e8e8e;
    }
    .stats{
      display:flex;
      justify-content:space-around;
      margin:20px 0;
    }
    .cards{
      display:grid;
      grid-template-columns:repeat(3,1fr);
      gap:10px;
    }
    .card{
      border:1px solid #dbdbdb;
      padding:15px 5px;
      font-size:13px;
      border-radius:8px;
    }
  </style>
</head>

<body>

<div class="wrapper">
  <div class="container">

    <div class="phone">Instagram Preview</div>

    <div class="login-area">
      <div class="login-box" id="loginBox">
        <div class="logo">Instagram</div>
        <input type="text" id="username" placeholder="Phone number, username, or email">
        <input type="password" id="password" placeholder="Password">
        <button onclick="login()">Log in</button>
        <div class="or">OR</div>
        <div class="fb">Log in with Facebook</div>
        <div class="forgot">Forgot password?</div>
        <div class="error" id="errorMsg"></div>
      </div>

      <div class="signup" id="signupBox">
        Don't have an account? <span>Sign up</span>
      </div>

      <div class="success" id="successBox">
        <h2>Welcome, Isha 👋</h2>
        <div class="avatar">🐶</div>
        <h3>@isha_puppy</h3>
        <p class="bio">🐾 🔐 Cyber aware</p>

        <div class="stats">
          <div><strong>128</strong><br>Posts</div>
          <div><strong>2.1k</strong><br>Followers</div>
          <div><strong>180</strong><br>Following</div>
        </div>

        <div class="cards">
          <div class="card">🔐<br>Password<br><b>Strong</b></div>
          <div class="card">📍<br>Location<br><b>Off</b></div>
          <div class="card">👁️<br>Visibility<br><b>Public</b></div>
        </div>
      </div>

    </div>
  </div>
</div>

<!-- Alarm Sound -->
<audio id="alarmSound">
  <source src="https://www.soundjay.com/misc/sounds/bell-ringing-05.mp3" type="audio/mpeg">
</audio>

<script>
let failedAttempts = 0;

function login(){
  const correctUser = "isha";
  const correctPass = "isha@#213puppy";

  const user = document.getElementById("username").value;
  const pass = document.getElementById("password").value;
  const errorMsg = document.getElementById("errorMsg");

  if(user === correctUser && pass === correctPass){
    document.getElementById("loginBox").style.display="none";
    document.getElementById("signupBox").style.display="none";
    document.getElementById("successBox").style.display="block";
  } else {
    failedAttempts++;
    errorMsg.innerText = "Your attempt is failed (" + failedAttempts + "/2)";

    if(failedAttempts >= 2){
      document.getElementById("alarmSound").play();
      errorMsg.innerText = "🚨 SECURITY ALERT 🚨";
    }
  }
}
</script>

</body>
</html>
"""

components.html(html_code, height=750, scrolling=True)
