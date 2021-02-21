import "./sample-content.js"

new Vue({
    el: "#app",
    data:
        function () {
            return {
                /* a negative test: this sholdn't appear */
                "content": "wrong content"
            }
        } 
  });
