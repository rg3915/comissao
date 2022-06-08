<template>
  <v-container
    id="user-profile"
    fluid
    tag="section"
  >
    <v-row justify="center">
      <v-col
        cols="12"
        md="8"
      >
        <base-material-card>
          <template v-slot:heading>
            <div class="text-h3 font-weight-light">
              Editar Pedido
            </div>

            <div class="text-subtitle-1 font-weight-light">
              Nº {{ item.id|pk }} - {{ item.customer.first_name }} {{ item.customer.last_name }} <br>
              {{ item.created|formatDate }}
            </div>
          </template>

          <v-form @submit.prevent="submitForm">
            <v-container class="py-0">
              <v-row>
                <v-col
                  cols="12"
                  md="6"
                >
                  <v-text-field
                    v-model="item.value"
                    class="purple-input"
                    label="Valor"
                  />
                </v-col>

                <v-col
                  cols="12"
                  md="6"
                >
                  <v-checkbox
                    v-model="item.paid"
                    label="Pago?"
                  ></v-checkbox>
                </v-col>

                <v-col
                  cols="12"
                  md="12"
                >
                <v-select
                  v-model="item.customer.id"
                  label="Cliente"
                  :items="customers"
                  ></v-select>
                </v-col>

                <v-col
                  cols="12"
                  class="text-right"
                >
                  <v-btn
                    color="success"
                    class="mr-0"
                    type="submit"
                  >
                    Salvar
                  </v-btn>
                </v-col>
              </v-row>
            </v-container>
          </v-form>
        </base-material-card>

        <base-material-card>
          <template v-slot:heading>
            <div class="text-h3 font-weight-light">
              Itens do Pedido
            </div>
          </template>

          <v-simple-table>
            <thead>
              <tr>
                <th class="text-center primary--text">
                  Quantidade
                </th>
                <th class="primary--text">
                  Serviço
                </th>
                <th class="text-right primary--text">
                  Preço
                </th>
                <th class="primary--text">
                  Funcionário
                </th>
                <th class="text-right primary--text">
                  Comissão
                </th>
              </tr>
            </thead>

            <tbody>
              <tr
                v-for="item in item.order_items"
                :key="item.id"
              >
                <td class="text-center">
                  {{ item.quantity }}
                </td>
                <td>{{ item.service.description }}</td>
                <td>R$ <span class="float-right">{{ item.price }}</span></td>
                <td>
                  {{ item.employee.user.first_name }} {{ item.employee.user.last_name }}
                </td>
                <td class="text-right">
                  {{ item.comission_employee|percentage }}%
                </td>
              </tr>
            </tbody>

            <tfoot>
              <tr>
                <td
                  class="text-h3 text-right"
                  colspan="2"
                >
                  Total
                </td>
                <td class="text-h3">
                  R$ <span class="float-right">{{ total }}</span>
                </td>
                <td>
                  <v-btn
                    color="primary"
                    class="mr-0"
                    @click="dialog = true"
                  >
                    Pagar
                  </v-btn>
                </td>
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
              </tr>
            </tfoot>
          </v-simple-table>
        </base-material-card>
      </v-col>

    </v-row>

    <v-dialog
      v-model="dialog"
      max-width="500"
    >
      <v-card class="text-center">
        <v-card-title>
          <div>
            <strong>Pedido: {{ item.id|pk }}</strong>
          </div>

          <div>
            <strong>Cliente: {{ item.customer.first_name }} {{ item.customer.last_name }}</strong>
          </div>

          <div>
            <strong>Data: {{ item.created|formatDate }}</strong>
          </div>

          <v-spacer />

          <v-icon
            aria-label="Close"
            @click="dialog = false"
          >
            mdi-close
          </v-icon>
        </v-card-title>

        <v-simple-table>
          <tbody>
            <tr>
              <td>Total a pagar</td>
              <td>R$ <span class="float-right">{{ total }}</span></td>
            </tr>
            <tr>
              <td>Pago</td>
              <td>R$ <span class="float-right">NaN <v-icon>mdi-emoticon-poop</v-icon></span></td>
            </tr>
            <tr>
              <td>Troco</td>
              <td>R$ <span class="float-right">NaN <v-icon>mdi-emoticon-poop</v-icon></span></td>
            </tr>
          </tbody>
        </v-simple-table>

        <v-card-actions>
          <v-spacer />

          <v-btn
            color="error"
            text
            @click="dialog = false"
          >
            Close
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-container>
</template>

<script>
  import axios from 'axios'

  export default {
    data () {
      return {
        dialog: false,
        item: {},
        customer_selected: {},
        customers: [],
      }
    },
    mounted () {
      this.getData()
      this.getCustomers()
    },
    computed: {
      total () {
        return this.item.order_items.reduce((acc, item) => acc + parseFloat(item.price), 0)
      },
    },
    methods: {
      getData () {
        const id = this.$route.params.id

        axios.get(`/api/v1/orders/${id}`)
          .then(response => {
            this.item = response.data
          })
      },
      getCustomers () {
        axios.get('/api/v1/customers')
          .then(response => {
            this.customers = response.data.map(obj => {
              return {
                value: obj.id,
                text: `${obj.first_name} ${obj.last_name}`,
              }
            })
          })
      },
      async submitForm () {
        const id = this.$route.params.id
        const item = { ...this.item }
        item.customer = item.customer.id

        axios
          .patch(`/api/v1/orders/${id}/`, item)
          .then(() => {
            this.$router.push({ name: 'Pedidos' })
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
        const string = date.split('-')
        const day = string[2].split('T')[0]
        return `${day}/${string[1]}/${string[0]}`
      },
    },
  }
</script>
