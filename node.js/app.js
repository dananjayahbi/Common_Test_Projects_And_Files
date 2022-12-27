var nodemailer = require('nodemailer');

var transporter = nodemailer.createTransport({
  service: 'gmail',
  auth: {
    user: 'isurudananjaya838@gmail.com',
    pass: 'Indusara'
  }
});

var mailOptions = {
  from: 'isurudananjaya838@gmail.com',
  to: 'dananjayahbi@gmail.com',
  subject: 'Sending Email using Node.js',
  text: 'That was easy!'
};

transporter.sendMail(mailOptions, function(error, info){
  if (error) {
    console.log(error);
  } else {
    console.log('Email sent: ' + info.response);
  }
});