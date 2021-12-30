let app = Vue.createApp({
    data() {
        return {
            count: 0
        }
    },
    mounted() {
        setInterval(() => {
            fetch('/api/tick')
            .then(response => response.json())
            .then(jsonResponse => {
                this.count = jsonResponse['tick'];
            });
        }, 2000);
    },
    template: "#app-template"
});
let vm = app.mount('#app');
