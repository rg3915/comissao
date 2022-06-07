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
        // Pages
        {
          name: 'User Profile',
          path: 'pages/user',
          component: () => import('@/views/dashboard/pages/UserProfile'),
        },
        {
          name: 'Notifications',
          path: 'components/notifications',
          component: () => import('@/views/dashboard/component/Notifications'),
        },
        {
          name: 'Icons',
          path: 'components/icons',
          component: () => import('@/views/dashboard/component/Icons'),
        },
        {
          name: 'Typography',
          path: 'components/typography',
          component: () => import('@/views/dashboard/component/Typography'),
        },
        // Tables
        {
          name: 'Regular Tables',
          path: 'tables/regular-tables',
          component: () => import('@/views/dashboard/tables/RegularTables'),
        },
        // Maps
        {
          name: 'Google Maps',
          path: 'maps/google-maps',
          component: () => import('@/views/dashboard/maps/GoogleMaps'),
        },
        // Upgrade
        {
          name: 'Upgrade',
          path: 'upgrade',
          component: () => import('@/views/dashboard/Upgrade'),
        },
        {
          name: 'Funcionários',
          path: 'pages/crm/employees',
          component: () => import('@/views/dashboard/pages/crm/Employees'),
        },
        {
          name: 'Funcionário',
          path: 'pages/crm/employee',
          component: () => import('@/views/dashboard/pages/crm/Employee'),
        },
        {
          name: 'Clientes',
          path: 'pages/crm/customers',
          component: () => import('@/views/dashboard/pages/crm/Customers'),
        },
        {
          name: 'Cliente',
          path: 'pages/crm/customer',
          component: () => import('@/views/dashboard/pages/crm/Customer'),
        },
        {
          name: 'Fornecedores',
          path: 'pages/crm/providers',
          component: () => import('@/views/dashboard/pages/crm/Providers'),
        },
        {
          name: 'Fornecedor',
          path: 'pages/crm/provider',
          component: () => import('@/views/dashboard/pages/crm/Provider'),
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
          name: 'Tipos de Avaliação',
          path: 'pages/services/evaluation-types',
          component: () => import('@/views/dashboard/pages/services/EvaluationTypes'),
        },
        {
          name: 'Produtos',
          path: 'pages/product/products',
          component: () => import('@/views/dashboard/pages/product/Products'),
        },
        {
          name: 'Produto',
          path: 'pages/product/product',
          component: () => import('@/views/dashboard/pages/product/Product'),
        },
        {
          name: 'Kits',
          path: 'pages/product/kits',
          component: () => import('@/views/dashboard/pages/product/Kits'),
        },
        {
          name: 'Kit',
          path: 'pages/product/kit',
          component: () => import('@/views/dashboard/pages/product/Kit'),
        },
        {
          name: 'Estoque Entrada',
          path: 'pages/stock/stock-entry',
          component: () => import('@/views/dashboard/pages/stock/StockEntries'),
        },
        {
          name: 'Estoque Saída',
          path: 'pages/stock/stock-exit',
          component: () => import('@/views/dashboard/pages/stock/StockExits'),
        },
        {
          name: 'Pagamentos',
          path: 'pages/financial/receivables',
          component: () => import('@/views/dashboard/pages/financial/Receivables'),
        },
        {
          name: 'Despesas',
          path: 'pages/financial/expenses',
          component: () => import('@/views/dashboard/pages/financial/Expenses'),
        },
        {
          name: 'Bancos',
          path: 'pages/financial/bank-accounts',
          component: () => import('@/views/dashboard/pages/financial/BankAccounts'),
        },
        {
          name: 'Tipos de Despesas',
          path: 'pages/financial/expense-types',
          component: () => import('@/views/dashboard/pages/financial/others/ExpenseTypes'),
        },
        {
          name: 'Categorias de Despesas',
          path: 'pages/financial/expense-categories',
          component: () => import('@/views/dashboard/pages/financial/others/ExpenseCategories'),
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
