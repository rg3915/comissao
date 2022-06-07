import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

export default new Router({
  mode: 'hash',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      component: () => import('@/views/dashboard/Index'),
      children: [
        // Dashboard
        {
          name: 'Dashboard',
          path: '',
          component: () => import('@/views/dashboard/Dashboard'),
        },
        {
          name: 'Funcionários',
          path: 'pages/crm/employees',
          component: () => import('@/views/dashboard/pages/crm/Employees'),
        },
        {
          name: 'Funcionário',
          path: 'pages/crm/employee/:id',
          component: () => import('@/views/dashboard/pages/crm/Employee'),
        },
        {
          name: 'Clientes',
          path: 'pages/crm/customers',
          component: () => import('@/views/dashboard/pages/crm/Customers'),
        },
        {
          name: 'Cliente',
          path: 'pages/crm/customer/:id',
          component: () => import('@/views/dashboard/pages/crm/Customer'),
        },
        {
          name: 'Pedidos',
          path: 'pages/services/orders',
          component: () => import('@/views/dashboard/pages/services/Orders'),
        },
        {
          name: 'Pedido',
          path: 'pages/services/order',
          component: () => import('@/views/dashboard/pages/services/Order'),
        },
        {
          name: 'Serviços',
          path: 'pages/services/services',
          component: () => import('@/views/dashboard/pages/services/Services'),
        },
        {
          name: 'Serviço',
          path: 'pages/services/service',
          component: () => import('@/views/dashboard/pages/services/Service'),
        },
        {
          name: 'Notas de Comissão',
          path: 'pages/financial/comission-notes',
          component: () => import('@/views/dashboard/pages/financial/notes/ComissionNotes'),
        },
        {
          name: 'Nota de Comissão',
          path: 'pages/financial/comission-note',
          component: () => import('@/views/dashboard/pages/financial/notes/ComissionNote'),
        },
      ],
    },
  ],
})
