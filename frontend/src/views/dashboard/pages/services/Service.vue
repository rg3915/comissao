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
              Editar Serviço
            </div>

            <!-- <div class="text-subtitle-1 font-weight-light">
              Complete your profile
            </div> -->
          </template>

          <v-form>
            <v-container class="py-0">
              <v-row>
                <v-col
                  cols="12"
                  md="12"
                >
                  <v-text-field
                    label="Descrição"
                    value="Sobrancelha"
                  />
                </v-col>

                <v-col
                  cols="12"
                  md="6"
                >
                  <v-text-field
                    class="purple-input"
                    label="Preço"
                  />
                </v-col>

                <v-col
                  cols="12"
                  md="6"
                >
                  <v-text-field
                    label="Comissão"
                    class="purple-input"
                  />
                </v-col>

                <v-col
                  cols="12"
                  md="12"
                >
                  <v-text-field
                    class="purple-input"
                    label="Kit"
                    value="Kit sobrancelha"
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
      </v-col>

      <base-material-card>
        <template v-slot:heading>
          <div class="text-h3 font-weight-light">
            Itens do Kit
          </div>
        </template>

        <v-simple-table>
          <thead>
            <tr>
              <th class="text-center primary--text">
                Quantidade
              </th>
              <th class="primary--text">
                Item
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
            </tr>
          </tbody>
        </v-simple-table>
      </base-material-card>

      <!-- <v-col
        cols="12"
        md="4"
      >
        <base-material-card
          class="v-card-profile"
        >
          <v-card-text class="text-center">
            <h6 class="display-1 mb-1 grey--text">
              CEO / CO-FOUNDER
            </h6>

            <h4 class="text-h3 font-weight-light mb-3 black--text">
              Alec Thompson
            </h4>

            <p class="font-weight-light grey--text">
              Don't be scared of the truth because we need to restart the human foundation in truth And I love you like Kanye loves Kanye I love Rick Owens’ bed design but the back is...
            </p>

            <v-btn
              color="success"
              rounded
              class="mr-0"
            >
              Follow
            </v-btn>
          </v-card-text>
        </base-material-card>
      </v-col> -->
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
