<template>
  <v-container
    id="regular-tables"
    fluid
    tag="section"
  >
    <v-btn
      tile
      color="primary"
      @click="goToCustomerAdd()"
    >
        <v-icon left>
          mdi-plus
        </v-icon>
        Adicionar
    </v-btn>
    <base-material-card
      icon="mdi-clipboard-text"
      title="Clientes"
      class="px-5 py-3"
    >
      <v-simple-table>
        <thead>
          <tr>
            <th class="primary--text">
              Nome
            </th>
            <th class="primary--text">
              E-mail
            </th>
            <th class="primary--text">
              Telefone
            </th>
          </tr>
        </thead>

        <tbody>
          <tr
            v-for="item in items"
            :key="item"
          >
            <td>
              <router-link :to="{ name: 'Cliente', params: { id: item.id }}">{{ item.first_name }} {{ item.last_name }}</router-link>
            </td>
            <td>{{ item.email }}</td>
            <td>{{ item.phone }}</td>
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
            first_name: 'Alec',
            last_name: 'Thompson',
            email: 'alec@thompson.com',
            phone: '97031-0000',
          },
          {
            first_name: 'Priscila',
            last_name: 'Jones',
            email: 'priscila@jones.com',
            phone: '91310-0101',
          },
          {
            first_name: 'Sage',
            last_name: 'Rodriguez',
            email: 'sage@rodriguez.com',
            phone: '94600-7600',
          },
          {
            first_name: 'Philip',
            last_name: 'Chaney',
            email: 'philip@chaney.com',
            phone: '98730-0050',
          },
          {
            first_name: 'Doris',
            last_name: 'Green',
            email: 'doris@green.com',
            phone: '95300-4503',
          },
        ],
      }
    },
    mounted () {
      this.getData()
    },
    methods: {
      getData () {
        axios.get('/api/v1/customers/')
          .then(response => {
            if (response.data.length) {
              this.items = response.data
            }
          })
      },
      goToCustomerAdd () {
        this.$router.push({ name: 'Adicionar Cliente' })
      },
    },
  }
</script>
