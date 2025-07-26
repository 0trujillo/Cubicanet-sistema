import { createRouter, createWebHistory } from 'vue-router'
import Dashboard from '../views/Dashboard.vue'
import CrudEmpleados from '../views/CrudEmpleados.vue'
import RegistroEntradaSalida from '../views/RegistroEntradaSalida.vue'

const routes = [
  { path: '/', name: 'Dashboard', component: Dashboard },
  { path: '/empleados', name: 'Empleados', component: CrudEmpleados },
  { path: '/registro', name: 'Registro', component: RegistroEntradaSalida }
]

export default createRouter({
  history: createWebHistory(),
  routes
})
