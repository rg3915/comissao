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
              Editar Fornecedor
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
                    value="Christina"
                  />
                </v-col>

                <v-col
                  cols="12"
                  md="4"
                >
                  <v-text-field
                    class="purple-input"
                    label="Sobrenome"
                    value="Powell"
                  />
                </v-col>

                <v-col
                  cols="12"
                  md="4"
                >
                  <v-text-field
                    class="purple-input"
                    label="Gênero"
                    value="Feminino"
                  />
                </v-col>

                <v-col
                  cols="12"
                  md="6"
                >
                  <v-text-field
                    class="purple-input"
                    label="E-mail"
                    value="crhistina@powell.com"
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
          avatar="https://randomuser.me/api/portraits/women/76.jpg"
        >
          <v-card-text class="text-center">
            <!-- <h6 class="text-h4 mb-1 grey--text">
              CEO / CO-FOUNDER
            </h6> -->

            <h4 class="text-h3 font-weight-light mb-3 black--text">
              Crhistina Powell
            </h4>

            <p class="font-weight-light grey--text">
              crhistina@powell.com
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
  </v-container>
</template>

<script>
  export default {
    //
  }
</script>
