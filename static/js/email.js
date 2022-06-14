/*
email.js is used by all pages.
Function to send email for newsletter sign up using emailjs.com.
*/

const newsletterFormCall = document.getElementById('newsletter-form');
/**
 * sendMail function uses the emailjs API to send the feedback to the site
 * owner when feedback is submitted.
 * The API used is from here - https://www.email.js.com/
 * Credit: Code Institute material "Sending Emails Using EmailJS"
 * @param {*} newsletterForm - The feedback form object
 */
function sendMail (newsletterForm) {
	emailjs.init('user_qNvMIMV6zD18pi4TUdgwz');
	emailjs.send('service_u0x86at', 'happiness-junkie-newsletter', {
		'from_email': newsletterForm.email.value,
	}).then(
		function (response) {
			success();
		},
		function (error) {
			console.log('Failed to send', error); // log error to console to allow inspection of error if it occurs
			failed();
		}
	);
	return false;
}