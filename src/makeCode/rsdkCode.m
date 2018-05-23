#import "rsdkCode.h"

@implementation rsdkCode
static rsdkCode *wrapperCode = nil;
+ (rsdkCode *)shareRsdkCode
{
    if (!wrapperCode) {
        wrapperCode = [[rsdkCode alloc] init];