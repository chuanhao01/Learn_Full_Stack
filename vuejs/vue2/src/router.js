import Vue from 'vue';
import Router from 'vue-router';

import Home from './views/Home';
import About from './views/About';

// Tells vue that it should use the Router
Vue.use(Router);

// Exports the router to be used in main.js
export default new Router({
    mode: 'history',
    routes: [
        {
            path: '/',
            component: Home
        },
        {
            path: '/about',
            component: About
        }
    ]
});

