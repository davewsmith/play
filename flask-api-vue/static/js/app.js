let app = Vue.createApp({
    data() {
        return {
            count: 0
        }
    },
    mounted() {
        setInterval(() => {
            this.count++;
        }, 1000);
    },
    template: "#app-template"
});
let vm = app.mount('#app');
