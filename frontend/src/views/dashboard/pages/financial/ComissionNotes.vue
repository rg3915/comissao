<template>
  <v-container
    id="regular-tables"
    fluid
    tag="section"
  >
    <base-material-card>
      <template v-slot:heading>
        <div class="text-h3 font-weight-light">
          Notas de Pagamento da Comissão
        </div>

        <div class="text-subtitle-1 font-weight-light">
          Para gerar uma Nota de Comissão escolha um Pedido e clique em "Gerar Nota de Comissão".
        </div>
      </template>
      <v-simple-table>
        <thead>
          <tr>
            <th class="primary--text">
              Nº
            </th>
            <th class="primary--text">
              Funcionário
            </th>
            <th class="primary--text text-center">
              Data de Pagamento
            </th>
            <th class="text-center primary--text">
              Pago
            </th>
          </tr>
        </thead>

        <tbody>
          <tr
            v-for="item in items"
            :key="item"
          >
            <td>
              <router-link :to="{ name: 'Nota de Comissão', params: { id: item.id }}">{{ item.id|pk }}</router-link>
            </td>
            <td>
              {{ item.employee.user.first_name }} {{ item.employee.user.last_name }}
            </td>
            <td class="text-center">
              {{ item.payment_date|formatDate }}
            </td>
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
        items: [],
      }
    },
    mounted () {
      this.getData()
    },
    methods: {
      getData () {
        axios.get('/api/v1/comissionnotes/')
          .then(response => {
            if (response.data.length) {
              this.items = response.data
            }
          })
        console.log(this.items)
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
      formatDate (date) {
        const string = date.split('-')
        const day = string[2].split('T')[0]
        return `${day}/${string[1]}/${string[0]}`
      },
    },
  }
</script>
