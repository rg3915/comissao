<template>
  <v-container
    id="regular-tables"
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
              Editar Kit
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
                    label="Título"
                    value="Kit para sobrancelha"
                  />
                </v-col>

                <v-col
                  cols="12"
                  md="6"
                >
                  <v-text-field
                    label="Descrição"
                    value="See reflect put big least whom."
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

                <v-col
                  cols="12"
                  md="12"
                >
                  <base-material-card
                    icon="mdi-clipboard-text"
                    title="Itens do Kit"
                    class="px-5 py-3"
                  >
                    <v-simple-table>
                      <thead>
                        <tr>
                          <th class="primary--text">
                            Quantidade
                          </th>
                          <th class="primary--text">
                            Produto
                          </th>
                          <th class="text-right primary--text">
                            Ações
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
                          <td>{{ item.description }}</td>
                          <td class="text-right">
                            <v-icon
                              class="mx-1"
                              style="color: red"
                            >
                              mdi-close
                            </v-icon>
                          </td>
                        </tr>
                        <tr>
                          <td>
                            <v-text-field placeholder="Quantidade" />
                          </td>
                          <td>
                            <v-text-field placeholder="Produto" />
                          </td>
                          <td>
                            <v-icon
                              class="mx-1"
                              style="color: green"
                            >
                              mdi-plus
                            </v-icon>
                          </td>
                        </tr>
                      </tbody>
                    </v-simple-table>
                  </base-material-card>
                </v-col>
              </v-row>
            </v-container>
          </v-form>
        </base-material-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
  export default {
    data () {
      return {
        items: [
          {
            id: 1,
            quantity: 1,
            description: 'Henna Ultra Fix profissional para sobrancelhas 2,5 g',
          },
          {
            id: 2,
            quantity: 1,
            description: 'Tesoura profissional para sobrancelhas',
          },
          {
            id: 3,
            quantity: 1,
            description: 'Pote copo de vidro para mistura',
          },
          {
            id: 4,
            quantity: 1,
            description: 'Pincel chanfrado aplicador',
          },
          {
            id: 5,
            quantity: 1,
            description: 'Palito para limpar',
          },
          {
            id: 6,
            quantity: 1,
            description: 'Paquímetro',
          },
          {
            id: 7,
            quantity: 3,
            description: 'Pinças reta, chanfrada',
          },
          {
            id: 8,
            quantity: 1,
            description: 'Mini depilador elétrico para sobrancelhas',
          },
        ],
      }
    },
  }
</script>
