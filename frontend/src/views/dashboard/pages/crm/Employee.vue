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
              Editar Funcionário
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
                    v-model="item.user.first_name"
                    label="Nome"
                  />
                </v-col>

                <v-col
                  cols="12"
                  md="6"
                >
                  <v-text-field
                    v-model="item.user.last_name"
                    class="purple-input"
                    label="Sobrenome"
                  />
                </v-col>

                <v-col
                  cols="12"
                  md="6"
                >
                  <v-text-field
                    v-model="item.user.email"
                    class="purple-input"
                    label="E-mail"
                  />
                </v-col>

                <v-col
                  cols="12"
                  md="6"
                >
                  <v-text-field
                    v-model="item.occupation"
                    label="Cargo"
                    class="purple-input"
                  />
                </v-col>

                <v-col
                  cols="12"
                  md="6"
                >
                  <v-text-field
                    v-model="item.cpf"
                    label="CPF"
                    class="purple-input"
                  />
                </v-col>

                <v-col
                  cols="12"
                  md="6"
                >
                  <v-text-field
                    v-model="item.rg"
                    label="RG"
                    class="purple-input"
                  />
                </v-col>

                <!-- <v-col cols="12">
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
                </v-col> -->

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
      </v-col>

      <v-col
        cols="12"
        md="4"
      >
        <base-material-card
          class="v-card-profile"
          avatar="https://cdn.pixabay.com/photo/2014/04/02/14/10/female-306407__340.png"
        >
          <v-card-text class="text-center">
            <!-- <h6 class="text-h4 mb-1 grey--text">
              CEO / CO-FOUNDER
            </h6> -->

            <h4 class="text-h3 font-weight-light mb-3 black--text">
              {{ item.user.first_name }} {{ item.user.last_name }}
            </h4>

            <p class="font-weight-light grey--text">
              {{ item.user.email }}
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

          </v-card-text>
        </base-material-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
  import axios from 'axios'

  export default {
    data () {
      return {
        item: {},
      }
    },
    mounted () {
      this.getData()
    },
    methods: {
      getData () {
        const id = this.$route.params.id

        axios.get(`/api/v1/employees/${id}`)
          .then(response => {
            this.item = response.data
          })
      },
      async submitForm () {
        const id = this.$route.params.id
        const item = { ...this.item }
        delete item.user.username

        axios
          .patch(`/api/v1/employees/${id}/`, item)
          .then(() => {
            this.$router.push({ name: 'Funcionários' })
          })
          .catch(error => {
            console.log(error)
          })
      },
    },
  }
</script>
