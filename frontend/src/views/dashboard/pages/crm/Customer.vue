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
              Editar Cliente
            </div>

            <!-- <div class="text-subtext-h6-1 font-weight-light">
              Complete your profile
            </div> -->
          </template>

          <v-form>
            <v-container class="py-0">
              <v-row>
                <v-col
                  cols="12"
                  md="4"
                >
                  <v-text-field
                    label="Nome"
                    value="Allison"
                  />
                </v-col>

                <v-col
                  cols="12"
                  md="4"
                >
                  <v-text-field
                    class="purple-input"
                    label="Sobrenome"
                    value="Watkins"
                  />
                </v-col>

                <v-col
                  cols="12"
                  md="4"
                >
                  <v-text-field
                    class="purple-input"
                    label="Gênero"
                    value="Masculino"
                  />
                </v-col>

                <v-col
                  cols="12"
                  md="6"
                >
                  <v-text-field
                    class="purple-input"
                    label="E-mail"
                    value="alisson@thompson.com"
                  />
                </v-col>

                <v-col
                  cols="12"
                  md="6"
                >
                  <v-text-field
                    label="Data de Nascimento"
                    class="purple-input"
                  />
                </v-col>

                <v-col
                  cols="12"
                  md="6"
                >
                  <v-text-field
                    label="CPF"
                    class="purple-input"
                  />
                </v-col>

                <v-col
                  cols="12"
                  md="6"
                >
                  <v-text-field
                    label="RG"
                    class="purple-input"
                  />
                </v-col>

                <v-col cols="12">
                  <v-text-field
                    label="Endereço"
                    class="purple-input"
                  />
                </v-col>

                <v-col
                  cols="12"
                  md="4"
                >
                  <v-text-field
                    label="Bairro"
                    class="purple-input"
                  />
                </v-col>

                <v-col
                  cols="12"
                  md="4"
                >
                  <v-text-field
                    label="Cidade"
                    class="purple-input"
                  />
                </v-col>

                <v-col
                  cols="12"
                  md="4"
                >
                  <v-text-field
                    class="purple-input"
                    label="CEP"
                    type="number"
                  />
                </v-col>

                <v-col
                  cols="12"
                  md="6"
                >
                  <v-text-field
                    class="purple-input"
                    label="Responsável"
                    value=""
                  />
                </v-col>

                <v-col
                  cols="12"
                  md="6"
                >
                  <v-text-field
                    label="Data de Nascimento"
                    class="purple-input"
                  />
                </v-col>

                <v-col
                  cols="12"
                  md="6"
                >
                  <v-text-field
                    label="CPF"
                    class="purple-input"
                  />
                </v-col>

                <v-col
                  cols="12"
                  md="6"
                >
                  <v-text-field
                    label="RG"
                    class="purple-input"
                  />
                </v-col>

                <!-- <v-col cols="12">
                  <v-textarea
                    class="purple-input"
                    label="About Me"
                    value="Lorem ipsum dolor sit amet, consectetur adipiscing elit."
                  />
                </v-col> -->

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

      <v-col
        cols="12"
        md="4"
      >
        <base-material-card
          class="v-card-profile"
          avatar="https://randomuser.me/api/portraits/men/26.jpg"
        >
          <v-card-text class="text-center">
            <!-- <h6 class="text-h4 mb-1 grey--text">
              CEO / CO-FOUNDER
            </h6> -->

            <h4 class="text-h3 font-weight-light mb-3 black--text">
              Allison Watkins
            </h4>

            <p class="font-weight-light grey--text">
              allison@watkins.com
            </p>

            <p class="font-weight-light grey--text">
              Indicado por Rose Martins.
            </p>

            <h5>Telefones</h5>

            <v-row>
              <v-col
                cols="12"
                md="12"
              >
                <div class="text-h6 font-weight-light">
                  Principal
                </div>
                <div class="text-h4 font-weight-light">
                  97532-0000
                </div>
              </v-col>

              <v-col
                cols="12"
                md="12"
              >
                <div class="text-h6 font-weight-light">
                  Residencial
                </div>
                <div class="text-h4 font-weight-light">
                  6082-3466
                </div>
              </v-col>
            </v-row>

            <v-row>
              <v-col>
                <v-btn
                  color="info"
                  class="mr-0"
                  @click="dialog = true"
                >
                  Avaliação
                </v-btn>
              </v-col>
            </v-row>

            <h5>Dados Bancários</h5>

            <v-row>
              <v-col
                cols="12"
                md="6"
              >
                <div class="text-h6 font-weight-light">
                  Nome do Banco
                </div>
                <div class="text-h4 font-weight-light">
                  NuBank
                </div>
              </v-col>

              <v-col
                cols="12"
                md="6"
              >
                <div class="text-h6 font-weight-light">
                  Nº do Banco
                </div>
                <div class="text-h4 font-weight-light">
                  260
                </div>
              </v-col>

              <v-col
                cols="12"
                md="6"
              >
                <div class="text-h6 font-weight-light">
                  Agência
                </div>
                <div class="text-h4 font-weight-light">
                  05352-0
                </div>
              </v-col>

              <v-col
                cols="12"
                md="6"
              >
                <div class="text-h6 font-weight-light">
                  Conta Corrente
                </div>
                <div class="text-h4 font-weight-light">
                  680435020
                </div>
              </v-col>
            </v-row>

            <!-- <v-btn
              color="success"
              rounded
              class="mr-0"
            >
              Follow
            </v-btn> -->
          </v-card-text>
        </base-material-card>
      </v-col>
    </v-row>

    <v-dialog
      v-model="dialog"
      max-width="500"
    >
      <v-card class="text-center">
        <v-card-text-h6>
          Avaliação do Cliente

          <v-spacer />

          <v-icon
            aria-label="Close"
            @click="dialog = false"
          >
            mdi-close
          </v-icon>
        </v-card-text-h6>

        <v-simple-table>
          <thead>
            <tr>
              <th class="primary--text">
                Tipo de Avaliação
              </th>
              <th class="text-right primary--text">
                Resposta
              </th>
            </tr>
          </thead>

          <tbody>
            <tr
              v-for="item in evaluations"
              :key="item"
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

        <v-card-actions>
          <v-spacer />

          <v-btn
            color="error"
            text
            @click="dialog = false"
          >
            Fechar
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
        evaluations: [
          {
            description: 'Está de rimel',
            response: true,
          },
          {
            description: 'Alergia a esmalte ou cosméticos',
            response: false,
          },
          {
            description: 'Problemas de tireóide',
            response: false,
          },
          {
            description: 'Algum procedimento feito recentemente nos olhos',
            response: false,
          },
          {
            description: 'Glaucoma/blefarite/algum problema ocular',
            response: true,
          },
          {
            description: 'Grávida',
            response: false,
          },
          {
            description: 'Tratamento oncológico',
            response: true,
          },
        ],
        dialog: false,
      }
    },
  }
</script>
