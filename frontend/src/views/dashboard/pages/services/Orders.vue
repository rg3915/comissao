<template>
  <v-container
    id="regular-tables"
    fluid
    tag="section"
  >
    <v-btn
      tile
      color="primary"
      @click="goToOrderAdd()"
    >
        <v-icon left>
          mdi-plus
        </v-icon>
        Adicionar
    </v-btn>
    <base-material-card
      icon="mdi-clipboard-text"
      title="Pedidos"
      class="px-5 py-3"
    >
      <v-simple-table>
        <thead>
          <tr>
            <th class="primary--text">
              Nº
            </th>
            <th class="primary--text">
              Cliente
            </th>
            <th class="primary--text">
              Valor
            </th>
            <th class="primary--text text-center">
              Pago?
            </th>
          </tr>
        </thead>

        <tbody>
          <tr
            v-for="item in items"
            :key="item"
          >
            <td>
              <router-link :to="{ name: 'Pedido', params: { id: item.id }}">{{ item.id|pk }}</router-link>
            </td>
            <td>{{ item.customer.first_name }} {{ item.customer.last_name }}</td>
            <td style="width: 150px">R$ <span class="float-right">{{ item.value }}</span></td>
            <td
              class="text-center"
              v-if="item.paid"
            >
              <v-icon
                class="mx-1"
                style="color: green"
              >
                mdi-check-bold
              </v-icon>
            </td>
            <td
              class="text-center"
              v-else
            >
              <v-icon
                class="mx-1"
                style="color: red"
              >
                mdi-close
              </v-icon>
            </td>
          </tr>
        </tbody>
      </v-simple-table>
    </base-material-card>
  </v-container>
</template>

<script>
  import axios from 'axios'

  export default {
    data () {
      return {
        items: [
          {
            id: '001',
            customer: {
              first_name: 'Dakota',
              last_name: 'Rice',
              email: 'dakota@email.com',
            },
            value: 180.00,
            paid: true,
          },
          {
            id: '002',
            customer: {
              first_name: 'Priscila',
              last_name: 'Jones',
              email: 'priscila@email.com',
            },
            value: 220.00,
            paid: true,
          },
          {
            id: '003',
            customer: {
              first_name: 'Sage',
              last_name: 'Rodriguez',
              email: 'sage@email.com',
            },
            value: 110.00,
            paid: true,
          },
          {
            id: '004',
            customer: {
              first_name: 'Philip',
              last_name: 'Chaney',
              email: 'philip@email.com',
            },
            value: 90.00,
            paid: false,
          },
          {
            id: '005',
            customer: {
              first_name: 'Doris',
              last_name: 'Green',
              email: 'doris@email.com',
            },
            value: 200.00,
            paid: false,
          },
        ],
      }
    },
    mounted () {
      this.getData()
    },
    methods: {
      getData () {
        axios.get('/api/v1/orders/')
          .then(response => {
            if (response.data.length) {
              this.items = response.data
            }
          })
      },
      goToOrderAdd () {
        this.$router.push({ name: 'Adicionar Pedido' })
      },
    },
    filters: {
      pk (id) {
        if (id < 10) {
          return `00${id}`
        }
        if (id < 100) {
          return `0${id}`
        }
        return id
      },
    },
  }
</script>
