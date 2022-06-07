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
              Nº 001 - 30/10/20 - Alec Thompson
            </div>
          </template>

          <v-form>
            <v-container class="py-0">
              <v-row>
                <v-col
                  cols="12"
                  md="4"
                >
                  <v-text-field
                    label="Data"
                    disabled
                  />
                </v-col>

                <v-col
                  cols="12"
                  md="4"
                >
                  <v-text-field
                    class="purple-input"
                    label="Hora Início"
                    disabled
                  />
                </v-col>

                <v-col
                  cols="12"
                  md="4"
                >
                  <v-text-field
                    class="purple-input"
                    label="Hora Final"
                    disabled
                  />
                </v-col>

                <v-col
                  cols="12"
                  md="12"
                >
                  <v-text-field
                    label="Cliente"
                    class="purple-input"
                    disabled
                  />
                </v-col>

                <v-col
                  cols="12"
                  class="text-right"
                >
                  <v-btn
                    color="success"
                    class="mr-0"
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
                v-for="item in items"
                :key="item.id"
              >
                <td class="text-center">
                  {{ item.quantity }}
                </td>
                <td>{{ item.service }}</td>
                <td>R$ <span class="float-right">{{ item.value }}</span></td>
                <td>
                  <s>{{ item.employee }}</s>
                </td>
                <td>
                  <s>{{ item.comission }}%</s>
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
                  R$ <span class="float-right">197,98</span>
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
                  <small>Pago?</small> <v-icon
                    class="mx-1"
                    style="color: green"
                  >
                    mdi-check-bold
                  </v-icon>
                </td>
              </tr>
            </tfoot>
          </v-simple-table>
        </base-material-card>
      </v-col>

      <v-col
        cols="12"
        md="4"
      >
        <base-material-card>
          <template v-slot:heading>
            <div class="text-h4 font-weight-light">
              Avaliação do Cliente
            </div>
          </template>

          <v-card-text class="text-center">
            <v-simple-table>
              <thead>
                <tr>
                  <th class="primary--text">
                    Avaliação
                  </th>
                  <th class="text-right primary--text">
                    Resposta
                  </th>
                </tr>
              </thead>

              <tbody>
                <tr
                  v-for="item in evaluations"
                  :key="item.id"
                >
                  <td class="text-left">
                    {{ item.description }}
                  </td>
                  <td v-if="item.response">
                    <v-icon
                      class="mx-1"
                      style="color: green"
                    >
                      mdi-check
                    </v-icon>
                  </td>
                  <td v-else>
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

            <h4 class="text-left ">
              Avaliação Adicional
            </h4>

            <v-simple-table>
              <thead>
                <tr>
                  <th class="primary--text">
                    Avaliação
                  </th>
                  <th class="text-right primary--text">
                    Resposta
                  </th>
                </tr>
              </thead>

              <tbody>
                <tr
                  v-for="item in aditional_evaluations"
                  :key="item.id"
                >
                  <td class="text-left">
                    {{ item.description }}
                  </td>
                  <td v-if="item.response">
                    <v-icon
                      class="mx-1"
                      style="color: green"
                    >
                      mdi-check
                    </v-icon>
                  </td>
                  <td v-else>
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
          </v-card-text>
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
            <strong>Pedido: 001</strong>
          </div>

          <div>
            <strong>Cliente: Alec Thompson</strong>
          </div>

          <div>
            <strong>Data: 30/10/2020</strong>
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
              <td>R$ <span class="float-right">120,00</span></td>
            </tr>
            <tr>
              <td>Pago</td>
              <td>R$ <span class="float-right">150,00</span></td>
            </tr>
            <tr>
              <td>Troco</td>
              <td>R$ <span class="float-right">30,00</span></td>
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
  export default {
    data () {
      return {
        dialog: false,
        items: [
          {
            id: 1,
            quantity: 1,
            service: 'Sobrancelha',
            value: 60.01,
            employee: 'Dona Watson',
            comission: 30,
          },
          {
            id: 2,
            quantity: 1,
            service: 'Depilação',
            value: 79.99,
            employee: 'Mara Lens',
            comission: 30,
          },
          {
            id: 3,
            quantity: 1,
            service: 'Mão',
            value: 23.99,
            employee: 'Jennifer Adrian',
            comission: 25,
          },
          {
            id: 4,
            quantity: 1,
            service: 'Pé',
            value: 33.99,
            employee: 'Jennifer Adrian',
            comission: 30,
          },
        ],
        evaluations: [
          {
            description: 'Alergia a esmalte ou cosméticos',
            response: false,
          },
          {
            description: 'Problemas de tireóide',
            response: false,
          },
          {
            description: 'Glaucoma/blefarite/algum problema ocular',
            response: true,
          },
          {
            description: 'Tratamento oncológico',
            response: true,
          },
        ],
        aditional_evaluations: [
          {
            description: 'Está de rimel',
            response: true,
          },
          {
            description: 'Algum procedimento feito recentemente nos olhos',
            response: false,
          },
          {
            description: 'Grávida',
            response: false,
          },
        ],
      }
    },
  }
</script>
