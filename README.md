# parser-cidades-municipios-ibge
Projeto para personalizar json de cidades e Estados do Brasil com dados retirados do ibge

### Como usar:

  - Instale o modulo requests
  - Instale o modulo json
  - Instale o modulo unidecode

### Formato do JSON atualmente:

```json5
[                                       // lista de Estados
  {
    "codigo": "11",                     // codigo do estado no IBGE
    "sigla": "RO",                      // sigla do Estado
    "nome": "RONDONIA",                 // nome do Estado
    "municipios": [                     // lista de municipios dentro deste Estado
      {
        "codigo": "1100015",            // codigo do municipio no IBGE
        "nome": "ALTA FLORESTA D'OESTE" // nome do municipio
      }
    ]
  }
]
```
