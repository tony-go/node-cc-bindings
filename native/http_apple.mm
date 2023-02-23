#include "include/http.h"

#import <Foundation/Foundation.h> // NSLog

namespace starship::raptor::http {

auto request() -> void {
  NSLog(@"Hello from OBJC!");
}

} // namespace starship::raptor::http
