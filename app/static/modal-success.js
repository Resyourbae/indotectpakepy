function showSuccessModal(message) {
    // Remove existing modal if any
    const existing = document.querySelector('.swal-overlay');
    if (existing) existing.remove();

    // Create the modal elements
    const overlay = document.createElement('div');
    overlay.className = 'swal-overlay';
    
    const modal = document.createElement('div');
    modal.className = 'swal-modal';
    
    // Create modal content
    modal.innerHTML = `
        <div class="swal-icon"></div>
        <h2 class="swal-title">Success!</h2>
        <p class="swal-text">${message}</p>
    `;
    
    overlay.appendChild(modal);
    document.body.appendChild(overlay);

    // Auto close after 2 seconds
    setTimeout(() => {
        overlay.classList.add('swal-closing');
        setTimeout(() => {
            overlay.remove();
        }, 300); // Match the animation duration
    }, 2000);
}

// Add the required styles
const style = document.createElement('style');
style.textContent = `
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    @keyframes fadeOut {
        from { opacity: 1; }
        to { opacity: 0; }
    }
    @keyframes modalSlide {
        from { transform: translate3d(0, -50px, 0); opacity: 0; }
        to { transform: translate3d(0, 0, 0); opacity: 1; }
    }
    @keyframes modalSlideOut {
        from { transform: translate3d(0, 0, 0); opacity: 1; }
        to { transform: translate3d(0, 50px, 0); opacity: 0; }
    }
    .animate-fadeIn {
        animation: fadeIn 0.3s ease-out;
    }
    .animate-fadeOut {
        animation: fadeOut 0.3s ease-in;
    }
    .animate-modalSlide {
        animation: modalSlide 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    }
    .animate-modalSlideOut {
        animation: modalSlideOut 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    }

    .success-checkmark {
        width: 80px;
        height: 80px;
        margin: 0 auto;
        border-radius: 50%;
        box-sizing: content-box;
        padding: 0;
    }
    .success-checkmark .check-icon {
        width: 80px;
        height: 80px;
        position: relative;
        border-radius: 50%;
        box-sizing: content-box;
        padding: 0;
    }
    .success-checkmark .check-icon::before {
        content: '';
        position: absolute;
        width: 80px;
        height: 80px;
        border-radius: 50%;
        background: #22c55e;
        transform: scale(0);
        animation: popInCircle 0.4s cubic-bezier(0.3, 1.5, 0.7, 1) forwards;
        opacity: 0;
    }
    .success-checkmark .check-icon .icon-line {
        height: 5px;
        background-color: #fff;
        display: block;
        border-radius: 2px;
        position: absolute;
        z-index: 10;
    }
    .success-checkmark .check-icon .icon-line.line-tip {
        top: 38px;
        left: 17px;
        width: 25px;
        transform: rotate(45deg);
        animation: iconLineTip 0.4s cubic-bezier(0.3, 1.5, 0.7, 1) 0.4s forwards;
        opacity: 0;
    }
    .success-checkmark .check-icon .icon-line.line-long {
        top: 32px;
        right: 14px;
        width: 47px;
        transform: rotate(-45deg);
        animation: iconLineLong 0.4s cubic-bezier(0.3, 1.5, 0.7, 1) 0.4s forwards;
        opacity: 0;
    }
    .success-checkmark .check-icon .icon-circle {
        position: absolute;
        top: 0;
        left: 0;
        z-index: 10;
        width: 80px;
        height: 80px;
        border-radius: 50%;
        box-sizing: content-box;
    }

    @keyframes popInCircle {
        from { 
            transform: scale(0);
            opacity: 0;
        }
        to { 
            transform: scale(1);
            opacity: 1;
        }
    }
    @keyframes iconLineTip {
        from {
            width: 0;
            left: 4px;
            opacity: 0;
        }
        to {
            width: 25px;
            left: 17px;
            opacity: 1;
        }
    }
    @keyframes iconLineLong {
        from {
            width: 0;
            right: 46px;
            opacity: 0;
        }
        to {
            width: 47px;
            right: 14px;
            opacity: 1;
        }
    }
`;
document.head.appendChild(style);
