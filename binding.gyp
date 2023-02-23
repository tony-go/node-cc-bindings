{
  "targets": [
    {
      "target_name": "hello",
      "sources": [ "hello.cc", "native/http_apple.mm" ],
      'defines': [ 'NAPI_DISABLE_CPP_EXCEPTIONS' ],
      "include_dirs": [
        "<!@(node -p \"require('node-addon-api').include\")"
      ],
      'xcode_settings': {
        'OTHER_CFLAGS': [
          "-std=c++20",
          "-I../native/include"
        ]
      }
    }
  ]
}
