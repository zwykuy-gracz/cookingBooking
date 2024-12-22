document.addEventListener("DOMContentLoaded", function () {
  const nameSearch = document.getElementById("name-search");
  const tags = document.querySelectorAll(".tag");
  const dishes = document.querySelectorAll(".project");

  function filterDish() {
    const nameQuery = nameSearch.value.toLowerCase();

    dishes.forEach((dish) => {
      const name = dish.getAttribute("data-name");
      const nameMatch = name.includes(nameQuery);
      console.log(nameMatch);

      if (nameMatch) {
        dish.style.display = "";
      } else {
        dish.style.display = "none";
      }
    });
  }

  tags.forEach((tag) => {
    tag.addEventListener("click", function () {
      const selectedTag = this.getAttribute("data-tag");

      dishes.forEach((dish) => {
        const dishTags = dish.getAttribute("data-tags");
        if (dishTags.includes(selectedTag)) {
          dish.style.display = "";
        } else {
          dish.style.display = "none";
        }
      });
    });
  });
  // TODO reset selected tags
  nameSearch.addEventListener("keyup", filterDish);
});
