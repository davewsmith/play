import {addTableComponent} from"./vue-table.js";

let app = Vue.createApp({
    data() {
        return {
            count: 0
        }
    },
    mounted() {
        this.timer = setInterval(() => {
            fetch('/api/tick')
            .then(
                response => {
                    if (response.ok) {
                        return response.json();
                    } else {
                        console.log('!response.ok');
                        clearInterval(this.timer);
                        return {'tick': -1};
                    }
                },
                networkError => {
                    console.log('networkError: ' + networkError.message);
                    clearInterval(this.timer);
                    return {'tick': networkError.message};
                })
            .then(jsonResponse => {
                this.count = jsonResponse['tick'];
            });
        }, 2000);
    },
    template: "#app-template"
});

addTableComponent(app);

let vm = app.mount('#app');


