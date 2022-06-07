<template>
  <v-container
    id="regular-tables"
    fluid
    tag="section"
  >
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
            name: 'Alec Thompson',
            email: 'alec@thompson.com',
            phone: '97031-0000',
          },
          {
            name: 'Priscila Jones',
            email: 'priscila@jones.com',
            phone: '91310-0101',
          },
          {
            name: 'Sage Rodriguez',
            email: 'sage@rodriguez.com',
            phone: '94600-7600',
          },
          {
            name: 'Philip Chaney',
            email: 'philip@chaney.com',
            phone: '98730-0050',
          },
          {
            name: 'Doris Green',
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
            this.items = response.data
          })
      },
    },
  }
</script>
