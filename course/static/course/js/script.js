//navbar
function openNav() {
  document.getElementById("mySlidenav").style.width = "250px";
  document.body.classList.add("open-menu");
 
}
function closeNav() {
  document.getElementById("mySlidenav").style.width = "0";
  document.body.classList.remove("open-menu");
}

//dropdown
const dropdowns = document.querySelectorAll(".mydropdown");

dropdowns.forEach((dropdown) => {
  const dropdownContent = dropdown.querySelector(".mydropdown-content");
  dropdown.addEventListener("click", (event) => {
    event.preventDefault();
    dropdownContent.classList.add("show");
  });
  document.addEventListener("click", (event) => {
    if (event.target.matches(".back-btn")) {
      event.preventDefault();

      dropdownContent.classList.add("hide");
      setTimeout(() => {
        dropdownContent.classList.remove("show");
        dropdownContent.classList.remove("hide");
        document.removeEventListener("click");
      }, 300);
    }
  });
});
