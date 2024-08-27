function myFunction() {
  x = document.getElementById('modif');
  if (x.contentEditable == "false") {
    x.contentEditable = "true";

  }
}


const getTitleMessageFromCategory = category => {
    const titles = {"success": "Well done",
                    "info": "Attention!",
                    "warning": "Attention!",
                    "error": "Oops!",


    }
    return titles[category]
    }
function showMessageAlert(category, message) {
    Swal.fire({
        icon: category,
        title: getTitleMessageFromCategory(category),
        text: message,

    })
}