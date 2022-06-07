<template>
  <v-container
    id="regular-tables"
    fluid
    tag="section"
  >
    <v-btn
      tile
      color="primary"
      @click="goToEmployeeAdd()"
    >
        <v-icon left>
          mdi-plus
        </v-icon>
        Adicionar
    </v-btn>
    <base-material-card
      icon="mdi-clipboard-text"
      title="Funcionários"
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
              Cargo
            </th>
          </tr>
        </thead>

        <tbody>
          <tr
            v-for="item in items"
            :key="item"
          >
            <td>
              <router-link :to="{ name: 'Funcionário', params: { id: item.id }}">{{ item.user.first_name }} {{ item.user.last_name }}</router-link>
            </td>
            <td>{{ item.user.email }}</td>
            <td>{{ item.occupation }}</td>
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
            user: {
              first_name: 'Alec',
              last_name: 'Thompson',
              email: 'alec@thompson.com',
            },
            occupation: 'Cabelereiro',
          },
          {
            user: {
              first_name: 'Priscila',
              last_name: 'Jones',
              email: 'priscila@jones.com',
            },
            occupation: 'Maquiador',
          },
          {
            user: {
              first_name: 'Sage',
              last_name: 'Rodriguez',
              email: 'sage@rodriguez.com',
            },
            occupation: 'Manicure',
          },
          {
            user: {
              first_name: 'Philip',
              last_name: 'Chaney',
              email: 'philip@chaney.com',
            },
            occupation: 'Cabelereiro',
          },
          {
            user: {
              first_name: 'Doris',
              last_name: 'Green',
              email: 'doris@green.com',
            },
            occupation: 'Depiladora',
          },
        ],
      }
    },
    mounted () {
      this.getData()
    },
    methods: {
      getData () {
        axios.get('/api/v1/employees/')
          .then(response => {
            console.log(response.data)
            console.log(response.data.length)
            if (response.data.length) {
              this.items = response.data
            }
          })
      },
      goToEmployeeAdd () {
        this.$router.push({ name: 'Adicionar Funcionário' })
      },
    },
  }
</script>
