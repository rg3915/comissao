<template>
  <v-container
    id="comission-note"
    fluid
    tag="section"
  >
    <base-material-card>
      <template v-slot:heading>
        <div class="text-h3 font-weight-light">
          Nota de Pagamento da Comissão
        </div>

        <div class="text-h2 font-weight-light">
          {{ item.employee.user.first_name }} {{ item.employee.user.last_name }}
        </div>
      </template>
      <v-form>
        <v-container class="py-0">
          <v-row>
            <v-col
              cols="12"
              md="6"
            >
              <v-text-field
                v-model="item.payment_date"
                label="Data de Pagamento"
                disabled
              />
            </v-col>

            <v-col
              cols="12"
              md="6"
            >
              <v-checkbox
                v-model="item.paid"
                label="Pago?"
                disabled
              ></v-checkbox>
            </v-col>

          </v-row>
        </v-container>
      </v-form>
      <v-simple-table>
        <thead>
          <tr>
            <th class="primary--text">
              Pedido
            </th>
            <th class="text-center primary--text">
              Quantidade
            </th>
            <th class="primary--text">
              Serviço
            </th>
            <th class="text-right primary--text">
              Valor da comissão
            </th>
          </tr>
        </thead>

        <tbody>
          <tr
            v-for="item in item.comission_note_items"
            :key="item.comission_note"
          >
            <td>{{ item.comission_note }}</td>
            <td class="text-center">
              {{ item.quantity }}
            </td>
            <td>{{ item.order_items.service.description }}</td>
            <td><span class="float-right">R$ {{ item.comission }}</span></td>
          </tr>
        </tbody>

        <tfoot>
          <tr>
            <td class="text-h3 font-weight-light text--primary">
              <small>Pago?</small>
              <v-icon
                class="mx-1"
                style="color: green"
                v-if="item.paid"
              >
                mdi-check-bold
              </v-icon>
              <v-icon
                class="mx-1"
                style="color: red"
                v-else
              >
                mdi-close
              </v-icon>
            </td>
            <td class="text-center">
              Data de pagto: {{ item.payment_date|formatDate }}
            </td>
            <td class="text-h3 text-right">
              Total
            </td>
            <td class="text-h2">
              <span class="float-right">R$ {{ total }}</span>
            </td>
          </tr>
        </tfoot>
      </v-simple-table>
    </base-material-card>
  </v-container>
</template>

<script>
  import axios from 'axios'

  export default {
    data () {
      return {
        item: {
          payment_date: '',
          paid: false,
        },
      }
    },
    mounted () {
      this.getData()
    },
    computed: {
      total () {
        return this.item.comission_note_items.reduce((acc, item) => acc + parseFloat(item.comission), 0)
      },
    },
    methods: {
      getData () {
        const id = this.$route.params.id

        axios.get(`/api/v1/comissionnotes/${id}`)
          .then(response => {
            this.item = response.data
          })
      },
      async submitForm () {
        const id = this.$route.params.id
        const item = { ...this.item }
        item.customer = item.customer.id

        axios
          .patch(`/api/v1/comissionnotes/${id}/`, item)
          .then(() => {
            this.$router.push({ name: 'Notas de Comissão' })
          })
          .catch(error => {
            console.log(error)
          })
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
      percentage (comission) {
        return comission * 100
      },
      formatDate (date) {
        if (!date) return

        const string = date.split('-')
        const day = string[2].split('T')[0]
        return `${day}/${string[1]}/${string[0]}`
      },
    },
  }
</script>
