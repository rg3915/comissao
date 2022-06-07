<template>
  <v-navigation-drawer
    id="core-navigation-drawer"
    v-model="drawer"
    :dark="barColor !== 'rgba(228, 226, 226, 1), rgba(255, 255, 255, 0.7)'"
    :expand-on-hover="expandOnHover"
    :right="$vuetify.rtl"
    :src="barImage"
    mobile-break-point="960"
    app
    width="260"
    v-bind="$attrs"
  >
    <template v-slot:img="props">
      <v-img
        :gradient="`to bottom, ${barColor}`"
        v-bind="props"
      />
    </template>

    <v-divider class="mb-1" />

    <v-list
      dense
      nav
    >
      <v-list-item>
        <v-list-item-avatar
          class="align-self-center"
          color="white"
          contain
        >
          <v-img
            src="https://demos.creative-tim.com/vuetify-material-dashboard/favicon.ico"
            max-height="30"
          />
        </v-list-item-avatar>

        <v-list-item-content>
          <v-list-item-title
            class="text-h4"
            v-text="profile.title"
          />
        </v-list-item-content>
      </v-list-item>
    </v-list>

    <v-divider class="mb-2" />

    <v-list
      expand
      nav
    >
      <!-- Style cascading bug  -->
      <!-- https://github.com/vuetifyjs/vuetify/pull/8574 -->
      <div />

      <template v-for="(item, i) in computedItems">
        <base-item-group
          v-if="item.children"
          :key="`group-${i}`"
          :item="item"
        >
          <!--  -->
        </base-item-group>

        <base-item
          v-else
          :key="`item-${i}`"
          :item="item"
        />
      </template>

      <!-- Style cascading bug  -->
      <!-- https://github.com/vuetifyjs/vuetify/pull/8574 -->
      <div />
    </v-list>

    <!-- <template v-slot:append>
      <base-item
        :item="{
          title: $t('upgrade'),
          icon: 'mdi-package-up',
          to: '/upgrade',
        }"
      />
    </template> -->
  </v-navigation-drawer>
</template>

<script>
  // Utilities
  import {
    mapState,
  } from 'vuex'

  export default {
    name: 'DashboardCoreDrawer',

    props: {
      expandOnHover: {
        type: Boolean,
        default: false,
      },
    },

    data: () => ({
      items: [
        /* {
          icon: 'mdi-view-dashboard',
          title: 'dashboard',
          to: '/',
        },
        {
          icon: 'mdi-account',
          title: 'user',
          to: '/pages/user',
        },
        {
          title: 'rtables',
          icon: 'mdi-clipboard-outline',
          to: '/tables/regular-tables',
        }, */
        /* {
          title: 'typography',
          icon: 'mdi-format-font',
          to: '/components/typography',
        },
        {
          title: 'icons',
          icon: 'mdi-chart-bubble',
          to: '/components/icons',
        },
        {
          title: 'google',
          icon: 'mdi-map-marker',
          to: '/maps/google-maps',
        },
        {
          title: 'notifications',
          icon: 'mdi-bell',
          to: '/components/notifications',
        }, */
        {
          title: 'Funcionários',
          icon: 'mdi-account',
          to: '/pages/crm/employees',
        },
        {
          title: 'Clientes',
          icon: 'mdi-account-group',
          to: '/pages/crm/customers',
        },
        {
          title: 'Fornecedores',
          icon: 'mdi-account-outline',
          to: '/pages/crm/providers',
        },
        {
          title: 'Pedidos',
          icon: 'mdi-clipboard-outline',
          to: '/pages/services/orders',
        },
        {
          title: 'Serviços',
          icon: 'mdi-hair-dryer',
          to: '/pages/services/services',
        },
        {
          title: 'Tipos de Avaliação',
          icon: 'mdi-clipboard-edit-outline',
          to: '/pages/services/evaluation-types',
        },
        {
          title: 'Produtos',
          icon: 'mdi-content-cut',
          to: '/pages/product/products',
        },
        {
          title: 'Kits',
          icon: 'mdi-chart-bubble',
          to: '/pages/product/kits',
        },
        {
          title: 'Estoque Entrada',
          icon: 'mdi-arrow-up-bold-box',
          to: '/pages/stock/stock-entry',
        },
        {
          title: 'Estoque Saída',
          icon: 'mdi-arrow-down-bold-box',
          to: '/pages/stock/stock-exit',
        },
        {
          title: 'Pagamentos',
          icon: 'mdi-currency-usd',
          to: '/pages/financial/receivables',
        },
        {
          title: 'Despesas',
          icon: 'mdi-currency-usd',
          to: '/pages/financial/expenses',
        },
        {
          title: 'Bancos',
          icon: 'mdi-bank',
          to: '/pages/financial/bank-accounts',
        },
        {
          title: 'Tipos de Despesas',
          icon: 'mdi-attachment',
          to: '/pages/financial/expense-types',
        },
        {
          title: 'Categorias de Despesas',
          icon: 'mdi-gamma',
          to: '/pages/financial/expense-categories',
        },
        {
          title: 'Notas de Comissão',
          icon: 'mdi-clipboard-text-outline',
          to: '/pages/financial/comission-notes',
        },
      ],
    }),

    computed: {
      ...mapState(['barColor', 'barImage']),
      drawer: {
        get () {
          return this.$store.state.drawer
        },
        set (val) {
          this.$store.commit('SET_DRAWER', val)
        },
      },
      computedItems () {
        return this.items.map(this.mapItem)
      },
      profile () {
        return {
          avatar: true,
          title: this.$t('avatar'),
        }
      },
    },

    methods: {
      mapItem (item) {
        return {
          ...item,
          children: item.children ? item.children.map(this.mapItem) : undefined,
          title: this.$t(item.title),
        }
      },
    },
  }
</script>

<style lang="sass">
  @import '~vuetify/src/styles/tools/_rtl.sass'

  #core-navigation-drawer
    .v-list-group__header.v-list-item--active:before
      opacity: .24

    .v-list-item
      &__icon--text,
      &__icon:first-child
        justify-content: center
        text-align: center
        width: 20px

        +ltr()
          margin-right: 24px
          margin-left: 12px !important

        +rtl()
          margin-left: 24px
          margin-right: 12px !important

    .v-list--dense
      .v-list-item
        &__icon--text,
        &__icon:first-child
          margin-top: 10px

    .v-list-group--sub-group
      .v-list-item
        +ltr()
          padding-left: 8px

        +rtl()
          padding-right: 8px

      .v-list-group__header
        +ltr()
          padding-right: 0

        +rtl()
          padding-right: 0

        .v-list-item__icon--text
          margin-top: 19px
          order: 0

        .v-list-group__header__prepend-icon
          order: 2

          +ltr()
            margin-right: 8px

          +rtl()
            margin-left: 8px
</style>
